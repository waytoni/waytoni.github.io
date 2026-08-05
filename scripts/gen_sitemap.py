"""
Generate sitemap.xml for a static website.

Usage:
  python gen_sitemap.py --site-root ../ --base-url https://example.com --output ../sitemap.xml

This script walks the site root directory, finds HTML files, and writes a sitemap.xml
including <loc> and <lastmod> tags. It ignores files and directories starting with
an underscore or a dot (common for hidden/system files), and skips 404 pages.
"""

from __future__ import annotations

import argparse
import os
import posixpath
from datetime import datetime, timezone
from xml.etree import ElementTree as ET


def iter_html_files(root: str):
	for dirpath, dirnames, filenames in os.walk(root):
		# skip hidden, underscore, and ignored dirs (testing, working)
		ignored_dirs = {"testing", "working", "scripts", "Homepage"}
		dirnames[:] = [
			d for d in dirnames
			if not d.startswith(".") and not d.startswith("_") and d.lower() not in ignored_dirs
		]
		for fname in filenames:
			if fname.startswith(".") or fname.startswith("_"):
				continue
			if not fname.lower().endswith(".html"):
				continue
			yield os.path.join(dirpath, fname)


def url_for(root: str, filepath: str, base_url: str) -> str:
	rel_path = os.path.relpath(filepath, root).replace(os.path.sep, "/")
	# map index.html to directory URL
	if rel_path.endswith("index.html"):
		rel_path = rel_path[: -len("index.html")]
	return posixpath.join(base_url.rstrip("/"), rel_path)


def file_lastmod(filepath: str) -> str:
	ts = os.path.getmtime(filepath)
	return datetime.fromtimestamp(ts, timezone.utc).date().isoformat()


def build_sitemap(site_root: str, base_url: str) -> ET.Element:
	urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
	for f in iter_html_files(site_root):
		# skip obvious 404 pages
		if os.path.basename(f).lower().startswith("404"):
			continue
		url = ET.SubElement(urlset, "url")
		loc = ET.SubElement(url, "loc")
		loc.text = url_for(site_root, f, base_url)
		lastmod = ET.SubElement(url, "lastmod")
		lastmod.text = file_lastmod(f)
	return urlset


def write_xml(elem: ET.Element, out_path: str) -> None:
	tree = ET.ElementTree(elem)
	# prettify: indent
	indent(elem)
	tree.write(out_path, encoding="utf-8", xml_declaration=True)


def indent(elem, level=0):
	i = "\n" + level * "  "
	if len(elem):
		if not elem.text or not elem.text.strip():
			elem.text = i + "  "
		for e in elem:
			indent(e, level + 1)
		if not e.tail or not e.tail.strip():
			e.tail = i
	else:
		if level and (not elem.tail or not elem.tail.strip()):
			elem.tail = i


DEFAULT_BASE_URL = "https://waytoni.com"


def main():
	p = argparse.ArgumentParser(description="Generate sitemap.xml for a static site")
	p.add_argument("--site-root", default=".", help="Path to site root directory (default: .)")
	p.add_argument("--base-url", default=DEFAULT_BASE_URL, help=f"Base URL (default: {DEFAULT_BASE_URL})")
	p.add_argument("--output", default="sitemap.xml", help="Output sitemap file path (default: sitemap.xml)")
	args = p.parse_args()

	urlset = build_sitemap(args.site_root, args.base_url)
	write_xml(urlset, args.output)


if __name__ == "__main__":
	main()

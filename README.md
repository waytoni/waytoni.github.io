# waytoni.github.io

This repository hosts the source code and content for the Dhamma lessons website featuring sermons by **Ajantha Sampath Guruthuma**.

<p align="center">
  <img src="images/favicon_wheel/android-chrome-192x192.png" alt="Way to Nibbana Logo" width="120">
</p>

---

## Guide: Updating the Website

This guide is designed for content editors and maintainers who may not have prior experience with Git or the command line.

---

### Part 1: Initial Setup (One-Time Only)

Before updating the site for the first time, make sure you have the following free tools installed:

1. **[Python 3](https://www.python.org/downloads/)** (or [Anaconda Distribution](https://www.anaconda.com/download))
   * *Windows users*: Be sure to check **"Add Python to PATH"** during installation.
2. **[Visual Studio Code (VS Code)](https://code.visualstudio.com/)**
3. **[GitHub Desktop](https://desktop.github.com/)**
4. *(Recommended)* **Five Server** or **Live Server** extension in VS Code for live browser preview.

#### Setting Up the Repository:
1. Open **GitHub Desktop** and log in with your GitHub account.
2. Go to **File** > **Clone Repository...**, select `waytoni.github.io` (or paste the repository URL), and choose a folder on your computer.
3. Once downloaded, open **VS Code**, go to **File** > **Open Folder...**, and select the `waytoni.github.io` folder.
4. Install the required Python packages:
   * In VS Code, open the integrated terminal by pressing `` Ctrl + ` `` (Windows) or `` Cmd + ` `` (Mac), or from the top menu **Terminal** > **New Terminal**.
   * Type the following command and press **Enter**:
     ```bash
     pip install -r requirements.txt
     ```

---

### Part 2: Day-to-Day Workflow for Adding New Videos

Follow these 5 simple steps whenever a new video or lecture needs to be added:

#### Step 1: Fetch Latest Changes
* Open **GitHub Desktop**.
* Click the **Fetch origin** button in the top toolbar.
* If updates are found, click **Pull origin** to ensure your local files are up to date.

---

#### Step 2: Add New Video Entry
1. Open the project in **VS Code**.
2. In the file explorer on the left, navigate to the active series folder under `current/` (for example, `current/MaharagamaB/`).
3. Open the corresponding `_ytlinks.txt` file (e.g., `current/MaharagamaB/MaharagamaB_ytlinks.txt`).
4. Scroll to the very bottom and add a new line using this format:
   ```text
   <index> [optional description/title] <YouTube URL> <Date>
   ```
   * **`<index>`**: The next sequential video number (e.g. if the previous line was `10`, use `11`).
   * **`[optional description/title]`**: Brief title or note from YouTube (Sinhala or English).
   * **`<YouTube URL>`**: Full YouTube link (e.g., `https://www.youtube.com/watch?v=...`).
   * **`<Date>`**: Date of the sermon in `YYYY-MM-DD` format (e.g., `2026-08-22`).

   **Example:**
   ```text
   11 නිවන් මග උදෙසා දර්ශන ඥානය https://www.youtube.com/watch?v=zJUU2Bn3gl8 2026-08-22
   ```

5. Save the file (`Ctrl + S` on Windows / `Cmd + S` on Mac).

---

#### Step 3: Build the Website
1. In VS Code, open [`build_it.py`](file:///Users/upul/Documents/GitHub/waytoni.github.io/build_it.py) from the root folder.
2. Run the script:
   * Go to the top menu: **Run** > **Run Without Debugging** (or press `Ctrl + F5` / `F5`).
   * Alternatively, in the terminal run:
     ```bash
     python build_it.py
     ```
3. Watch the terminal at the bottom — you should see confirmation messages that HTML and JSON files were generated successfully.

---

#### Step 4: Preview Your Changes Locally
1. In VS Code's file tree, locate `index.html` (or the specific series `.html` file).
2. Right-click the file and select **Open with Five Server** (or **Open with Live Server**).
3. Check the page in your browser to confirm that the new video appears correctly with its link and notes.

---

#### Step 5: Publish Changes Online
1. Switch back to **GitHub Desktop**.
2. You will see a list of modified files on the left panel (the updated text file, generated HTML, and JSON files).
3. At the bottom-left:
   * In the **Summary** box, write a brief note (e.g., `Add video 11 to Maharagama B`).
   * Click the blue **Commit to main** button.
4. Click **Push origin** in the top bar.

> [!NOTE]
> Once pushed, GitHub Pages will automatically deploy the changes. The live website will update within 1–2 minutes.

---

### Troubleshooting & FAQs

* **Error: Missing Python libraries**
  * Run `pip install -r requirements.txt` in the VS Code terminal.
* **Python interpreter not selected in VS Code**
  * Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac), type **Python: Select Interpreter**, and select your installed Python or Anaconda version.
* **The new video doesn't appear on the page**
  * Check that you ran `build_it.py` after editing the `_ytlinks.txt` file.
  * Ensure the video link in `_ytlinks.txt` is in the standard format (`https://www.youtube.com/watch?v=VIDEO_ID`).

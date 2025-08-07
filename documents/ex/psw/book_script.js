

document.addEventListener('DOMContentLoaded', function() {
    // ========== Audio Player Implementation ==========
    const audioSections = [{
        id: 'toc-ind-0-audio',
        title: 'සංඥාපනය',
        audioFile: 'audio/0_preface.mp3',
        elementId: 'toc-ind-0' // ID of the section element
      }, {
        id: 'toc-ind-1-audio',
        title: 'පටිච්ච සමුප්පාද විවරණය',
        audioFile: 'audio/1_intro.mp3',
        elementId: 'toc-ind-1'
      }, {
        id: 'toc-ind-6-audio',
        title: 'අවිජ්ජාපච්චයා සංඛාරා',
        audioFile: 'audio/2_aps.mp3',
        elementId: 'toc-ind-6'
      }, {
        id: 'toc-ind-8-audio',
        title: 'සංඛාරපච්චයා විඤ්ඤාණං',
        audioFile: 'audio/3_spv.mp3',
        elementId: 'toc-ind-8'
      }
    ];

    const audioPlayer = document.getElementById('main-audio-player');
    const audioTracksDiv = document.getElementById('audio-tracks');
    const nowPlayingDiv = document.getElementById('now-playing');
    let audioPositions = loadPositions();

    function loadPositions() {
        const saved = localStorage.getItem('audioPositions');
        return saved ? JSON.parse(saved) : {};
    }

    function savePositions() {
        localStorage.setItem('audioPositions', JSON.stringify(audioPositions));
    }

    function initAudioPlayer() {
        createAudioButtons();
        setupAudioEventListeners();
        addResetButton();
    }

    function createAudioButtons() {
        audioSections.forEach(section => {
            const btn = document.createElement('button');
            btn.className = 'audio-btn';
            btn.textContent = section.title;
            
            btn.addEventListener('click', () => {
                playAudioSection(section);
                document.getElementById('audio-player-container').classList.add('expanded');
            });
            
            audioTracksDiv.appendChild(btn);
        });
    }

    function playAudioSection(section) {
        // Save current position before switching
        if (audioPlayer.src) {
            const currentFile = getFilenameFromUrl(audioPlayer.src);
            audioPositions[currentFile] = audioPlayer.currentTime;
            savePositions();
        }

        nowPlayingDiv.textContent = `Now Playing: ${section.title}`;
        
        // Only change source if different
        const audioPath = new URL(section.audioFile, window.location.href).href;
        if (audioPlayer.src !== audioPath) {
            audioPlayer.src = audioPath;
            
            // Wait for metadata to load before setting position
            const onLoaded = () => {
                audioPlayer.currentTime = audioPositions[section.audioFile] || 0;
                audioPlayer.play().catch(e => {
                    console.log("Playback requires user interaction");
                    nowPlayingDiv.textContent += " (Click play button)";
                });
                audioPlayer.removeEventListener('loadedmetadata', onLoaded);
            };
            
            audioPlayer.addEventListener('loadedmetadata', onLoaded);
        } else {
            // Same file - just set position and play
            audioPlayer.currentTime = audioPositions[section.audioFile] || 0;
            audioPlayer.play().catch(e => {
                console.log("Playback requires user interaction");
                nowPlayingDiv.textContent += " (Click play button)";
            });
        }
        
        updateActiveButton(section.id);
    }

    function updateActiveButton(sectionId) {
        document.querySelectorAll('.audio-btn').forEach(btn => {
            btn.classList.remove('active');
            if (btn.textContent === sectionId) {
                btn.classList.add('active');
            }
        });
    }

    function addResetButton() {
        const resetBtn = document.createElement('button');
        resetBtn.className = 'audio-btn reset-btn';
        resetBtn.textContent = '↻ Reset';
        resetBtn.addEventListener('click', () => {
            if (audioPlayer.src) {
                const currentFile = getFilenameFromUrl(audioPlayer.src);
                audioPositions[currentFile] = 0;
                audioPlayer.currentTime = 0;
                savePositions();
                audioPlayer.play().catch(e => console.log("Play prevented:", e));
            }
        });
        audioPlayer.insertAdjacentElement('afterend', resetBtn);
    }

    function getFilenameFromUrl(url) {
        try {
            const urlObj = new URL(url);
            return urlObj.pathname.split('/').pop();
        } catch {
            return url.split('/').pop();
        }
    }

    function setupAudioEventListeners() {
        document.getElementById('toggle-audio-btn').addEventListener('click', () => {
            document.getElementById('audio-player-container').classList.toggle('expanded');
        });

        audioPlayer.addEventListener('pause', () => {
            if (audioPlayer.src) {
                const currentFile = getFilenameFromUrl(audioPlayer.src);
                audioPositions[currentFile] = audioPlayer.currentTime;
                savePositions();
            }
        });

        audioPlayer.addEventListener('error', () => {
            nowPlayingDiv.textContent = "Error playing audio";
            console.error("Audio error:", audioPlayer.error);
        });
    }

    // ========== Font Controls ==========
    const contentContainer = document.querySelector('.content-container');
    const defaultFontSize = 16;
    let currentFontSize = defaultFontSize;

    function initFontControls() {
        const savedFontSize = localStorage.getItem('fontSize');
        if (savedFontSize) {
            currentFontSize = parseInt(savedFontSize);
            contentContainer.style.fontSize = `${currentFontSize}px`;
        }

        document.getElementById('increase-font').addEventListener('click', () => {
            currentFontSize = Math.min(currentFontSize + 1, 24);
            updateFontSize();
        });

        document.getElementById('decrease-font').addEventListener('click', () => {
            currentFontSize = Math.max(currentFontSize - 1, 12);
            updateFontSize();
        });

        document.getElementById('reset-font').addEventListener('click', () => {
            currentFontSize = defaultFontSize;
            updateFontSize();
        });
    }

    function updateFontSize() {
        contentContainer.style.fontSize = `${currentFontSize}px`;
        localStorage.setItem('fontSize', currentFontSize.toString());
    }

    // ========== Initialize ==========
    initAudioPlayer();
    initFontControls();
});
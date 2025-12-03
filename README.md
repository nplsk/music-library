# jfh-view

A set of tools for displaying a local music library on a web interface.

**Background and ideas:**  
[Project planning document](https://docs.google.com/document/d/1xcNdlIfbqIN5MVHyVnceiRLx-8G4bPj5zbAf5KZB12s/edit?usp=sharing)

---

## Requirements

- [Node.js](https://nodejs.org/en/download)

---

## Planned Features

### File Scanning

- Get track length
- Fetch Discogs links

### Rekordbox Integration

- Parse `rekordbox.yml`
- Generate `prepared.json` from Rekordbox library
- Extract metadata (e.g. star ratings)

### YouTube Track Previews

- Play button on tile hover
- YouTube player overlay in bottom-right corner
- Backend: `get_yt_link(artist, title, length?)`
- Auto-play related tracks by spatial proximity (x, y) on canvas

### Display Modes

- Toggle between canvas and list view
- Album art: inline or in pop-up
- Playlist handling:
  - Read `.m3u` or similar
  - Use for grouping into islands
- 2D Canvas View:
  - Frontend-based placement (allows UI control)
  - Hex island layout with improved spacing
  - Square/rectangular layout options
  - Search and filtering
  - Genre proximity logic:
    - Similar genres placed closer together
    - Venn-style overlapping for tracks with multiple genres
- List View:
  - Tree/file structure view
  - Sorting/filtering via [List.js](https://listjs.com)
- File Reveal:
  - Open file in OS directory (like Soulseek)

### General UI

- Title bar with:
  - Library name
  - Current view label
  - Date created
  - Stats (e.g., track count)
- Favicon support (low priority)
- Mobile UX:
  - Pinch-to-zoom
  - Improved panning
  - Click-to-select
- Liked tracks playlist:
  - Heart icon on hover
  - Sidebar list
  - Export as `.txt` or YouTube playlist

### Performance

- Test with large libraries (e.g., 2000+ tracks)
- Investigate dynamic loading/chunking
- Limit zoom-out to only render visible tiles
- Monitor `prepared.json` size for scalability

### Extended Integrations

- Discogs collection/wantlist `.csv`
- Other library exports:
  - Serato
  - Engine
  - iTunes
- Bandcamp:
  - [bandcamp-library-scraper](https://github.com/dbeley/bandcamp-library-scraper)
- Streaming services (future scope)
- Custom pages for DJ mixes/originals

### Long-term Ideas

- Chatroom integration
- Per-track message boards
- 3D visualisation:
  - Low-poly museum-style rooms
  - Hidden interactive elements
- Liked track collection/exporting

---

## Backend Setup

The backend scripts require Python and some dependencies.

1.  **Install Python**: Ensure you have Python 3.8+ installed.
2.  **Install Dependencies**:
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

---

## How to Import Your Library

You can import your music library from a local folder or a Rekordbox XML export.

### Option A: Scan a Music Folder
To scan a directory of audio files (mp3, flac, wav, etc.):

```bash
python backend/import_library.py --music-dir "/path/to/your/music"
```

### Option B: Import from Rekordbox XML
1.  Export your collection (or a playlist) from Rekordbox as XML.
2.  Run the import script:

```bash
python backend/import_library.py --rekordbox-xml "/path/to/rekordbox.xml"
```

**Optional: Filter by Playlist**
If you only want to import a specific playlist from the XML:

```bash
python backend/import_library.py --rekordbox-xml "/path/to/rekordbox.xml" --playlist "My Top Tracks"
```

---

## Frontend Setup

The React app lives in the `/frontend` directory.

### Run the App

1.  **Install Node Dependencies**:
    ```bash
    cd frontend
    npm install
    ```

2.  **Start the Dev Server**:
    ```bash
    npm run dev
    ```

The app will be available at `http://localhost:5173` (or similar).

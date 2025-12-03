import argparse
from pathlib import Path
import sys
import os

# Add current directory to path so we can import local modules
sys.path.append(str(Path(__file__).parent))

from scan_library import scan_library
from prepare_metadata import main as prepare_main

def main():
    parser = argparse.ArgumentParser(description="Import music library for jfh-view")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--music-dir", type=Path, help="Path to the music directory to scan")
    group.add_argument("--rekordbox-xml", type=Path, help="Path to Rekordbox XML file")
    
    parser.add_argument("--playlist", type=str, help="Playlist name to filter (only for Rekordbox XML)")
    parser.add_argument("--output", type=Path, default=Path("../frontend/public/prepared.json"), help="Path to output JSON file")
    
    args = parser.parse_args()
    
    # Resolve paths
    base_dir = Path(__file__).resolve().parent
    
    # Intermediate output path
    intermediate_json = base_dir.parent / "data" / "json" / "output.json"
    
    # Run scan_library
    print(f"--- Step 1: Scanning Library ---")
    try:
        scan_library(
            music_dir=args.music_dir,
            rekordbox_xml_path=args.rekordbox_xml,
            playlist_name=args.playlist,
            output_path=intermediate_json
        )
    except Exception as e:
        print(f"Error during scanning: {e}")
        return

    # Run prepare_metadata
    print(f"\n--- Step 2: Preparing Metadata ---")
    
    # Resolve output path relative to current working directory if not absolute, 
    # or relative to script location if default
    if args.output.is_absolute():
        final_output = args.output
    else:
        # If user provided a relative path, treat it relative to CWD
        # If default was used, it's relative to script location (handled by default value logic usually, but let's be safe)
        if str(args.output) == "../frontend/public/prepared.json":
             final_output = base_dir / args.output
        else:
             final_output = Path.cwd() / args.output

    try:
        prepare_main(intermediate_json, final_output)
        print(f"\n✅ Success! Library imported to {final_output}")
        print(f"You can now run the frontend to view your library.")
    except Exception as e:
        print(f"Error during metadata preparation: {e}")

if __name__ == "__main__":
    main()

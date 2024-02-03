import os
import json


def main():
    root_path = "src/content/notes"
    dirs = sorted(os.listdir(root_path))

    result = {
        "title": "My Notes",
        "path": "/notes",
        "routes": [
            # {"hasSectionHeader": True, "sectionHeader": "GET STARTED"},
            # {
            #     "title": "Quick Start",
            #     "path": "/learn",
            #     "routes": [
            #         {"title": "Tutorial: Tic-Tac-Toe", "path": "/learn/tutorial-tic-tac-toe"},
            #         {"title": "Thinking in React", "path": "/learn/thinking-in-react"},
            #     ],
            # },
        ],
    }

    for d in dirs:
        if os.path.isfile(f"{root_path}/{d}"):
            continue
        markdown_files = sorted(os.listdir(f"{root_path}/{d}"))

        dirname = d.replace(".md", "")
        if dirname == "index":
            continue
        hasheader = {"hasSectionHeader": True, "sectionHeader": dirname}
        result["routes"].append(hasheader)

        temp = {
            "title": dirname,
            "path": f"/notes/{dirname}",
            "routes": [],
        }
        for mf in markdown_files:
            mfname = mf.replace(".md", "")
            if mfname == "index":
                continue
            temp["routes"].append({"title": mfname, "path": f"/notes/{dirname}/{mfname}"})

        result["routes"].append(temp)

    with open("src/sidebarNotes.json", "w") as file:
        file.write(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()

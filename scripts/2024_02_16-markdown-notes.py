import re


def parse_markdown_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Splitting the content into sections based on dates
    date_sections = re.split(r'\n## \d{4}-\d{2}-\d{2}', content)[1:]  # Skip the first empty split

    notes_data = []

    for section in date_sections:
        # Further split each section into individual notes
        notes = re.split(r'\n### ', section)

        for note in notes:
            if note.strip():
                # Extracting metadata and description
                metadata_match = re.search(r'- metadata: ([^,]+), #(.+)', note)
                date_time = metadata_match.group(1) if metadata_match else None
                tags = metadata_match.group(2).split(', #') if metadata_match else []

                # Extract the title and content
                title_match = re.match(r'(.+?)\n', note)
                title = title_match.group(1) if title_match else 'Untitled'
                content = note.split('---')[1].strip() if '---' in note else note

                notes_data.append({
                    'date_time': date_time,
                    'tags': tags,
                    'title': title,
                    'content': content
                })

    return notes_data


if __name__ == "__main__":
    filename = '....md'
    notes_mapping = parse_markdown_file(filename)
    print(notes_mapping)

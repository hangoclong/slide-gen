# Slides Generator Project

This project is designed to automate the creation of interactive HTML slide presentations from Markdown-formatted textbook chapters. It also includes functionality to generate structured JSON prompts for AI image generation, allowing for the creation of visually rich and engaging educational content.

## Features

*   **Markdown to HTML Conversion:** Transforms raw Markdown chapter files into single, self-contained HTML slide presentations.
*   **Interactive Slides:** Generated HTML presentations include navigation controls, theme switching, and options for exporting individual slides or the entire presentation to PDF.
*   **AI Image Prompt Generation:** Analyzes slide content to create detailed JSON prompts for AI image generators, focusing on ultra-realistic, human-centric visuals in a vertical format.
*   **Pedagogical Elements:** Integrates learning objectives, knowledge checks, in-class assignments (with AI support prompts), and summary slides.
*   **Mermaid Diagram Support:** Renders simple Mermaid diagrams within the slides for conceptual visualization.
*   **Customizable Theming:** Supports multiple visual themes for the presentations.

## Project Structure

```
slides-gen/
├── raw-chapters/                 # Input Markdown files for textbook chapters
├── slides-gen/                   # Output directory for HTML presentations and generated image prompts
│   ├── information-system-today-chapter-1.html  # Example HTML slide presentation
│   ├── information-system-today-chapter-4.html  # Generated HTML slide presentation
│   └── information-system-today-chapter-4.md    # Generated JSON image prompts for Chapter 4
├── SampleTemplate.html           # Base HTML template used for generating slides
├── IMG-GEN-PROMPT.md             # Instructions and format for AI image prompt generation
├── SYSTEM-INSTRUCTION.md         # Detailed system instructions for the slide generation agent
├── requirements.txt              # Python dependencies for the project
├── setup_environment.sh          # Script to set up the Python virtual environment
├── generate_image.py             # (Potentially) Script for image generation based on prompts
└── README.md                     # This README file
```

## How to Use

1.  **Prepare Chapter Content:** Place your Markdown-formatted textbook chapter files (e.g., `Information-Systems-Today-9th-Part-4.md`) into the `raw-chapters/` directory.
2.  **Generate Slides:** Provide the path to your Markdown chapter file and the `SampleTemplate.html` to the slide generation agent. The agent will process the content, create an interactive HTML presentation, and save it in the `slides-gen/` directory.
3.  **Generate Image Prompts:** The agent will also identify slides requiring visual content (e.g., two-panel layouts) and generate corresponding JSON prompts, following the guidelines in `IMG-GEN-PROMPT.md`, saved as a `.md` file in the `slides-gen/` directory.
4.  **View Presentation:** Open the generated HTML file in a web browser to view the interactive slides.
5.  **Generate Images (External Step):** Use the generated JSON prompts with an AI image generation tool to create the actual images, which can then be integrated into the HTML slides.

## Setup

To set up the project environment, it is recommended to use a Python virtual environment:

```bash
bash setup_environment.sh
```

This script will create a `venv` directory and install the necessary Python packages listed in `requirements.txt`.

## Contributing

Contributions are welcome! Please refer to `SYSTEM-INSTRUCTION.md` for guidelines on how to interact with the slide generation agent and maintain project conventions.

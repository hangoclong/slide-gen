# PRIMARY PROMPT

Read @SYSTEM-INSTRUCTION.md and @slides-gen/syllabus.md . Do it carefully I want more than 50 slides, including mermaid chart (Simple only, do not add special characters or " or " or parentheses). I want interactive class, which contain inclass quiz or in-class assignment like short 30 mins (with ChatGPT or Google Gemini AI support).  

INPUT:@raw-chapters/Information-Systems-Today-9th-Part-1.md 
OUPUT: /slides-gen slide with similar structure of @information-system-today-chapter-1.html and similar name like information-system-today-chapter-x



# SECONDARY PROMPT

## OPTION 1 (If no img placeholders in output .html file)
Suggest 10 slides number for me. It should have meaningful or rich information and potential provide content high-quality image generation (like canva). E.g., Slide x. Put those snippets html into a .md file with similar name with the html file in /slides-gen/ 

## OPTION 2 (If existing placeholers in output .html file)
Read @IMG-GEN-PROMPT.md carefully for instruction. 
Let pick the html snippet of your slides that contain placeholder images, then Put those generated json from snippets html into a .md file with similar name with the html file in /slides-gen/ 

## NEXT
Pick each json snippet above, then run the python command below with parameter "YOUR_PROMPT_HERE" is replaced by each json. Generated images should have similar name of header above json snippet, like slide-2.png and store in above created @img-information-system-today-chapter-x (parameter "./output_directory")

```bash
# Complete one-liner for image generation
source venv/bin/activate && python generate_image.py "YOUR_PROMPT_HERE" ./output_directory
```


# => IMAGE PROMPT GEN
https://aistudio.google.com/prompts/1vP8_3s95j5TZrnhbiWz1fYJMtMqc1wzs

### System Prompt: The JSON Prompt Generator

You are an Expert Prompt Engineer specializing in creating visual prompts for AI image generators. Your mission is to translate raw text from a presentation slide into a structured **JSON object**. This JSON will serve as a complete and effective prompt to generate a single, ultra-realistic, human-centric photograph in a vertical format.

REMEMBER: The character must be Vietnamese female (prefer) or young male

**Your Process:**

1.  **Analyze & Distill:** Read the user's slide text and identify the single core concept, theme, or emotion (e.g., "complexity," "strategy," "collaboration," "security").
2.  **Brainstorm a Human Metaphor:** Conceive a powerful, real-world photographic scene involving people that metaphorically represents the distilled concept. This is the creative core of your task.
3.  **Construct the JSON:** Build a detailed JSON object based on your brainstormed metaphor, strictly adhering to the structure and style rules defined below.

**JSON Structure and Content Rules:**

You must generate a JSON object with the following four top-level keys: `prompt`, `negative_prompt`, `style_and_composition`, and `technical_parameters`.

1.  **`prompt` (string):**
    *   This is a detailed, vivid description of the photographic scene.
    *   Describe the people (their appearance, actions, expressions), the environment, and the overall action.
    *   Focus on creating a story or a moment in time.

2.  **`negative_prompt` (string):**
    *   This is a critical, comma-separated list of elements to forbid.
    *   **Always include:** `CGI, 3D render, abstract, illustration, diagram, chart, futuristic, glowing lines, blue interface, text, icons, symbols, unrealistic, cartoon, graphic.`

3.  **`style_and_composition` (object):**
    *   This object must contain four keys: `aesthetic`, `lighting`, `camera_shot`, and `mood`.
    *   **`aesthetic`**: Use keywords like `professional photography, corporate lifestyle, authentic, candid, high-end stock photo, sharp focus`.
    *   **`lighting`**: Use keywords like `natural light, bright soft lighting, cinematic lighting, professional studio lighting`.
    *   **`camera_shot`**: Use keywords like `medium shot, close-up on hands, over-the-shoulder shot, shallow depth of field, bokeh background`.
    *   **`mood`**: Use keywords that match the concept, like `focused, collaborative, optimistic, serious, innovative, secure`.

4.  **`technical_parameters` (object):**
    *   This object must contain two keys: `aspect_ratio` and `quality`.
    *   **`aspect_ratio`**: Must always be `"9:16"`.
    *   **`quality`**: Must always be `"ultra-realistic, photorealistic, 8k"`.

**Examples of Your Task:**

*   **If User Input is:** `<h1>Challenges of Globalization</h1> <ul><li>Governmental</li><li>Geoeconomic</li><li>Cultural</li></ul>`
    *   **Your Output (Raw JSON):**
        ```json
        {
          "prompt": "A vertical, professional photograph of a diverse team of business executives in a modern, sunlit conference room. They are gathered around a large table, leaning in to look at a complex map on a tablet. Their expressions are serious and focused, engaged in intense problem-solving and collaborative discussion.",
          "negative_prompt": "CGI, 3D render, abstract, illustration, diagram, chart, futuristic, glowing lines, blue interface, text, icons, symbols, unrealistic, cartoon, graphic.",
          "style_and_composition": {
            "aesthetic": "professional photography, corporate lifestyle, authentic, candid, sharp focus",
            "lighting": "bright soft lighting, natural light from a large window",
            "camera_shot": "medium shot, shallow depth of field, focus on faces and tablet",
            "mood": "serious, collaborative, focused, intellectual"
          },
          "technical_parameters": {
            "aspect_ratio": "9:16",
            "quality": "ultra-realistic, photorealistic, 8k"
          }
        }
        ```

*   **If User Input is:** `<h2>The Six Important Business Objectives</h2>`
    *   **Your Output (Raw JSON):**
        ```json
        {
          "prompt": "A vertical, ultra-realistic photograph from an over-the-shoulder perspective. A female architect in a modern office is making a precise final mark with a pencil on a large, complex blueprint spread across her desk. The focus is on her hand and the blueprint.",
          "negative_prompt": "CGI, 3D render, abstract, illustration, diagram, chart, futuristic, glowing lines, blue interface, text, icons, symbols, unrealistic, cartoon, graphic.",
          "style_and_composition": {
            "aesthetic": "professional photography, authentic, sharp focus, clean",
            "lighting": "professional studio lighting, focused on the desk",
            "camera_shot": "close-up, over-the-shoulder shot, shallow depth of field, bokeh background",
            "mood": "focused, precise, strategic, determined"
          },
          "technical_parameters": {
            "aspect_ratio": "9:16",
            "quality": "ultra-realistic, photorealistic, 8k"
          }
        }
        ```

**Final Instruction:** Your entire response must be **only the raw JSON object**. Do not write any explanations. Do not wrap the JSON in markdown backticks.

# ==> NANO BANANA 
https://aistudio.google.com/prompts/1PcI1XqxF0v5Zhq7bnjFuqdaLeCVLyqWr


# PUT IMAGE TO SLIDES

Check all images in @slides-gen/img-information-system-today-chapter-1/ and place each into its corresponding slide. Position the image flush to either the left or right edge, spanning the full vertical height (top to bottom) in a Canva-style two-panel layout. Maintain aspect ratio, avoid cropping when possible, and reserve the opposite side as a clean text column with safe margins (no text over the image). If the side choice is ambiguous, default to left on odd-numbered slides and right on even-numbered slides.
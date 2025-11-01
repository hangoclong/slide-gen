REST

#!/bin/bash
set -e -E

GEMINI_API_KEY="$AIzaSyAiXRI4U-wC3YXp5dbmFlQwkV-_GHibf88"
MODEL_ID="gemini-2.5-flash-image"
GENERATE_CONTENT_API="streamGenerateContent"

cat << EOF > request.json
{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "INSERT_INPUT_HERE"
          },
        ]
      },
    ],
    "generationConfig": {
      "responseModalities": ["IMAGE", "TEXT", ],
      "imageConfig": {
        "aspectRatio": "9:16",
        "image_size": "1K"
      },
    },
}
EOF

curl \
-X POST \
-H "Content-Type: application/json" \
"https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:${GENERATE_CONTENT_API}?key=${GEMINI_API_KEY}" -d '@request.json'

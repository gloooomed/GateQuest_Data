import os
import json
import glob
import sys
from jsonschema import validate, ValidationError, SchemaError

# Define the expected schema
schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "year": {"type": "integer"},
        "questionNumber": {"type": "integer"},
        "subject": {"type": "string"},
        "topic": {"type": "string"},
        "questionType": {"type": "string"},
        "question": {"type": "string"},
        "options": {
            "type": "array",
            "items": {"type": "string"}
        },
        "correctAnswer": {
            "oneOf": [
                {
                    "type": "array",
                    "items": {"type": "integer"}
                },
                {
                    "type": "number"
                },
            ]
        },
        "answerText": {"type": ["string", "null"]},
        "difficulty": {"type": "string"},
        "marks": {"type": "integer"},
        "tags": {
            "type": "array",
            "items": {"type": "string"}
        },
        "source": {"type": "string"},
        "sourceURL": {"type": "string"},
        "addedBy": {"type": "string"},
        "verified": {"type": "boolean"},
        "explanation": {"type": "string"},
        "metadata": {
            "type": "object",
            "properties": {
                "set": {"type": "string"},
                "paperType": {"type": "string"},
                "language": {"type": "string"}
            },
            "required": ["set", "paperType", "language"]
        }
    },
    "required": [
        "id", "year", "questionNumber", "subject", "topic", "questionType",
        "question", "options", "correctAnswer", "answerText", "difficulty",
        "marks", "tags", "source", "sourceURL", "addedBy", "verified",
        "explanation", "metadata"
    ]
}

def validate_question(question):
    try:
        validate(instance=question, schema=schema)
        return True
    except ValidationError as e:
        print(f"Validation error: {e.message} in question ID {question.get('id')}")
        return False
    except SchemaError as e:
        print(f"Schema error: {e.message}")
        return False

def validate_file(json_file):
    print(f"\n🔍 Validating file: {json_file}")
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("Expected a list of questions.")
            for q in data:
                if not validate_question(q):
                    print(f"❌ Invalid question with ID {q.get('id')}")
            print(f"✅ Successfully validated {len(data)} questions in {json_file}")
    except json.JSONDecodeError:
        print(f"❌ Error decoding JSON in file: {json_file}")
    except Exception as e:
        print(f"❌ Error validating {json_file}: {e}")

def main():
    args = sys.argv[1:]

    if len(args) == 1:
        path = args[0]
        if os.path.isfile(path):
            validate_file(path)
        elif os.path.isdir(path):
            json_files = glob.glob(os.path.join(path, '*.json'))
            print(f"📁 Found {len(json_files)} JSON files in {path}")
            for file in json_files:
                validate_file(file)
        else:
            print(f"⚠️ Path not found: {path}")
    else:
        # No argument = validate all
        print("🌍 Validating all split_chunks/*/*.json files...")
        json_files = glob.glob('**/split_chunks/*.json', recursive=True)
        print(f"📄 Found {len(json_files)} JSON files.")
        for file in json_files:
            validate_file(file)

if __name__ == "__main__":
    main()

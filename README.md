# Clinical Link And Retrieval Assistant (CLARA)

Clinical Link And Retrieval Assistant (CLARA) is an AI-powered system designed to assist clinicians by answering natural language questions based on a patient’s medical history. Basing on [Completely OpenSource Retrieval Augmented Generation (CORAG)](https://github.com/harinaralasetty/CORAG), it uses Retrieval-Augmented Generation (RAG) combined with an agent-driven architecture to deliver accurate, context-aware responses grounded in structured and unstructured patient data. 

## Overview
CLARA processes a patient's medical records—including history of medical conditions, clinical notes, lab results, imaging summaries, and more through a mixture of RAG and LLM based architecture. When a user asks a question, the system retrieves relevant historical data, constructs a tailored prompt, and uses a large language model (LLM) to generate an informed answer. The system also supports uploading of medical documents to extract and store the data. 

**Note:** This is a work in progress; not all features are fully implemented yet.

## Key Features
- Patient-Aware Q&A: CLARA intelligently responds to questions using only the relevant portions of a patient’s medical history.
- Agent-Based Reasoning: A custom agent dynamically decides when to retrieve data, run tools, or invoke the LLM.
- Modular Data Ingestion: Supports ingestion from multiple data formats (e.g., PDFs, structured data, audio transcripts).
- Contextual Memory: Maintains awareness of prior queries to ensure continuity in longitudinal interactions.

## Flow

![Flowchart](https://github.com/harinaralasetty/CLARA/blob/main/CLARA.png)

## Getting Started

### Prerequisites

- Python environment with necessary dependencies.

### Installation

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure API keys in `config.py`:
   - Set your Google Vertex API key from [Google AI Studio](https://aistudio.google.com/)
   - Set your Serper API key from [SerpAPI Dashboard](https://serpapi.com/dashboard) if you intend to use the search tool.

3. Adjust chunk settings in `config.py` as needed.

### Running the Application

To start the server, execute:

```bash
streamlit run server_streamlit.py
```

## Screenshots

![Screenshot](https://github.com/harinaralasetty/CLARA/blob/main/screenshot.png)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache-2.0 license.

## Contact

For any questions or feedback, please contact us on LinkedIn: [Hari Naralasetty](https://www.linkedin.com/in/hnaralasetty/), [Poojith NGR](https://www.linkedin.com/in/poojith-ngr/)

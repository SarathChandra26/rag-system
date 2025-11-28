import argparse
from ingestion.ingest import ingest_pdf
from orchestrator.rag_controller import rag_answer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ingest", help="PDF to ingest")
    parser.add_argument("--query", help="Ask question")

    args = parser.parse_args()

    if args.ingest:
        ingest_pdf(args.ingest)

    if args.query:
        print("\nANSWER:\n")
        print(rag_answer(args.query))

if __name__ == "__main__":
    main()

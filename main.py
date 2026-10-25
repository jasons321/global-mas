import sys
from pipeline import run_pipeline


def main():
  if len(sys.argv) > 1:
    query = " ".join(sys.argv[1:])
  else:
    # Default query with implicit Western infrastructure assumptions
    query = (
        "What is the best way to design a patient scheduling app for primary"
        " care clinics?"
    )

  run_pipeline(query)


if __name__ == "__main__":
  main()
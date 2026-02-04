# SDET Prep Site - Command Manual

all: help

help:
	@echo "SDET Prep Commands"
	@echo "------------------"
	@echo "make serve            - Start the local development server"
	@echo "make build            - Build the final static site"
	@echo "make check-companies  - Toggle company interview status"
	@echo "make check-concepts   - Toggle Java concepts status"
	@echo "make check-programs   - Toggle Java programs status"
	@echo "make check-categorized - Toggle categorized questions status"
	@echo "make focus            - List all started tasks across the project"
	@echo "make clean            - Remove build artifacts"

# Start the Hugo development server
serve:
	hugo server

# Build the final static site
build:
	hugo --minify

# Interactive task manager for company questions
check-companies:
	python3 toggle_table.py content/12_company_based_questions/_index.md

# Interactive task manager for Java concepts
check-concepts:
	python3 toggle_table.py content/java-questions-bank/concepts/_index.md

# Interactive task manager for Java programs
check-programs:
	python3 toggle_table.py content/java-questions-bank/programs/_index.md

# Interactive task manager for categorized questions
check-categorized:
	python3 toggle_table.py content/java-questions-bank/categorized-questions/_index.md

# List all items marked as 'Started' ([-])
focus:
	python3 focus_view.py

# Clean up build artifacts
clean:
	rm -rf public resources
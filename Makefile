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
	@echo "make publish          - Build and deploy to GitHub Pages"

# Start the Hugo development server
serve:
	hugo server

# Build the final static site
build:
	hugo --minify

# Publish to GitHub Pages
publish: clean build
	@echo "Publishing to GitHub..."
	# Push Source
	git add .
	git commit -m "Site update" || true
	git push origin master
	# Push Public
	cd public && \
	git init && \
	git checkout -b gh-pages && \
	git add . && \
	git commit -m "Deploy site" && \
	git remote add origin https://github.com/notxkcd/sdet-prep-site.git && \
	git push --force origin gh-pages
	@echo "Deployed Successfully!"

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
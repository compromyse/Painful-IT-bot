build:
	docker build -t painful .
run:
	docker run -d painful
dev:
	docker run -it -v $(pwd):/painful_files_dev painful

.PHONY server:
server:
	uvicorn upload_handler:app --reload
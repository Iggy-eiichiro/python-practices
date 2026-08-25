import logging

# logging.basicConfig(
#     filename="app.log", level = logging.DEBUG 
# )


# logging.basicConfig( # it is not working because of missing "\app log" in r"c:\Users\bro\OneDrive\デスクトップ\python Rikai"
#     filename=r"c:\Users\bro\OneDrive\デスクトップ\python Rikai", level = logging.DEBUG
# )

logging.basicConfig(
    filename=r"c:\Users\bro\OneDrive\デスクトップ\python Rikai\app log", level = logging.DEBUG 
)
logging.debug("Debug message")
logging.info("User logged in")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
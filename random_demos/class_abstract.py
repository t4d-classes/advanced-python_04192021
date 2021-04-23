from abc import ABC, abstractmethod


class Logger(ABC):
    
    @abstractmethod
    def log(self, msg: str) -> None:
        pass

class FileLogger(Logger):

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def log(self, msg: str) -> None:
        with open(self.file_name, "a") as log_file:
            log_file.write(f"{msg}\n")

# logger = FileLogger("log.txt")
# logger.log("test")

class ConsoleLogger(Logger):

    def log(self, msg: str) -> None:
        print(msg)

# logger = ConsoleLogger()
# logger.log("test")

def do_it(logger: Logger) -> None:
    logger.log("did it")


do_it(FileLogger("log.txt"))
do_it(ConsoleLogger())
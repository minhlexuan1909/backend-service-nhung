from fastapi import HTTPException, status


class UserExistedException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_409_CONFLICT, 
            detail={
                "message": "Username has already existed"
            }
        )

class UnauthorizedException(HTTPException):
    def __init__(self, message=None) -> None:
        message = "Incorrect API Key" if message == None else message
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail={
                "message": message
            }
        )

class DeviceNotFound(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail={
                "message": "Device not found"
            }
        )

class QueueFullException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail={
                "message": "Queue is full"
            }
        )

class InvervalServerError(HTTPException):
    def __init__(self, message=None) -> None:
        message = message if message != None else "Interval Server Error"
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail={
                "message": message
            }
        )

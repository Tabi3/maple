from flask import Flask
from flask_cors import CORS

import asyncio

app : Flask = Flask(__name__)
CORS(app, supports_credentials=True)

class API():

    def _is_url_type(self, function: any) -> bool:
        if isinstance(function, list):
            return True
        return type(function).__name__ == 'method'

    def set_methods(methods = list()) -> any:
        def function(f):
            return [f, methods]
        return function

    def __new__(cls, path = None) -> "API":
        obj        : "API"     = object.__new__(cls)
        obj.path   : str       = path or cls.__name__
        properties : list[str] = obj.__dir__()

        for class_property in properties:
            property_value = obj.__getattribute__(class_property)
            if API._is_url_type(..., property_value):
                methods = ["GET"]
                if isinstance(property_value, list):
                    property_value, methods = property_value

                obj.__setattr__(
                    class_property, 
                    app.route(f'/{obj.path}/{class_property}', methods=methods)
                    (property_value)
                )
        
        return obj

class KhubAPI(API):

    @API.set_methods(methods=["POST", "GET"])
    async def test() -> tuple[any, int]:
        return {"message": "success"}, 200


async def main(*args, **kwargs) -> None:
    KhubAPI()
    app.run(port=5174, debug=True)


if __name__ == "__main__":
    asyncio.run(main())
#from jsonschema import validate

from src.enum.global_enums import GlobalErrorMessages

class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code
        self.parsed_object = None


    def validate(self, schema):
    # Проверяем, есть ли поле 'data' в ответе (обычная структура API с пагинацией)
        if isinstance(self.response_json, dict) and 'data' in self.response_json:
            data_to_validate = self.response_json['data']
        else:
            data_to_validate = self.response_json
    
    # Валидируем данные
        if isinstance(data_to_validate, list):
            for item in data_to_validate:
                parsed_object = schema.model_validate(item)
                self_parsed_object = parsed_object
        else:
            schema.model_validate(data_to_validate)
    
        return self

    # def validate(self, schema):
    #     if isinstance(self.response_json, list):
    #         for item in self.response_json:
    #             parsed_object = schema.model_validate(item)
    #             self_parsed_object = parsed_object

    #     else:
    #         schema.model_validate(self.response_json)

    
    # def validate(self, schema):
    # # Извлекаем данные из ответа API
    # # Если есть поле 'data', используем его, иначе используем весь response_json
    #     data_to_validate = self.response_json.get('data', self.response_json)
    
    #     if isinstance(data_to_validate, list):
    #         for item in data_to_validate:
    #             schema.model_validate(item)
    #     else:
    #         schema.model_validate(data_to_validate)
    
    #     return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value.format
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value.format
        return self 
    

    def get_parsed_object(self):
        return self.parsed_object



    def _str_(self):
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json}"


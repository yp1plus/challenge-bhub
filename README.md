# challenge-bhub

## How to run?
1. Activate the environment using `source venv/bin/activate`
2. Use `python -m unittest` to run the tests
3. Use `flask run` to execute the API

## API Documentation

### GET /clients

#### Parameters
No parameters

#### Request Body
No request body

#### Response body
Status Code: 200

Example:
```
[
    {
        "address": "16 Gurney Road",
        "bankAccounts": [],
        "companyName": "bhub",
        "invoicing": 18000.0,
        "phoneNumber": "+5574981325602",
        "registrationDate": "12/08/2022"
    }
]
```

### POST /clients
#### Parameters
No parameters

#### Request Body
```
{
    "type": "object",
    "properties": {
        "companyName": { "type": "string" },
        "phoneNumber": { "type": "string" },
        "address": { "type": "string" },
        "registrationDate": { "type": "string" },
        "invoicing": { "type": "number" },
        "bankAccounts": { 
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "codeBank": { "type": "string" },	
                    "agencyNumber": { "type": "string" },
                    "accountNumber": { "type": "string" }
                }
            }
        }
    }
}
```


#### Response body
Status Code: 200

Example:
```
    {
        "address": "16 Gurney Road",
        "bankAccounts": [],
        "companyName": "bhub",
        "invoicing": 18000.0,
        "phoneNumber": "+5574981325602",
        "registrationDate": "12/08/2022"
    }
```

### GET /clients/<companyName>
#### Parameters
companyName: string

#### Request Body
No request body


#### Response body
Status Code: 200

Example:
```
    {
        "address": "16 Gurney Road",
        "bankAccounts": [],
        "companyName": "bhub",
        "invoicing": 18000.0,
        "phoneNumber": "+5574981325602",
        "registrationDate": "12/08/2022"
    }
```


### PUT /clients/<companyName>
#### Parameters
companyName: string

#### Request Body
```
{
    "type": "object",
    "properties": {
        "phoneNumber": { "type": "string" },
        "address": { "type": "string" },
        "invoicing": { "type": "number" }
    }
}
```


#### Response body
Status Code: 200

Example:
```
    {
        "address": "16 Gurney Road",
        "bankAccounts": [],
        "companyName": "bhub",
        "invoicing": 18000.0,
        "phoneNumber": "+5574981325602",
        "registrationDate": "12/08/2022"
    }
```

### DELETE /clients/<companyName>
#### Parameters
companyName: string

#### Request Body
No request body


#### Response body
Status Code: 200

Example:
```
    Deleted with success
```

### GET /clients/<companyName>/bankAccounts
#### Parameters
companyName: string

#### Request Body
No request body

#### Response body
Status Code: 200

Example:
```
[
    {
        "accountNumber": "009922",
        "agencyNumber": "0080",
        "codeBank": "0040",
        "companyName": "bhub",
        "id": "49929993-a5ef-454e-9c72-566d9c4945f0"
    },
    {
        "accountNumber": "0099",
        "agencyNumber": "0080",
        "codeBank": "0040",
        "companyName": "bhub",
        "id": "0d15560f-ad2c-41b5-b439-1b919087ee69"
    }
]
```

### POST /clients/<companyName>/bankAccounts
#### Parameters
companyName: string

#### Request Body
```
{
    "type": "object",
    "properties": {
        "agencyNumber": { "type": "string" },
        "accountNumber": { "type": "string" },
        "codeBank": { "type": "string" }
    }
}
```

#### Response body
Status Code: 200

Example:
```
    {
        "accountNumber": "009922",
        "agencyNumber": "0080",
        "codeBank": "0040",
        "companyName": "bhub",
        "id": "49929993-a5ef-454e-9c72-566d9c4945f0"
    }
```

### GET /clients/bankAccounts/<id>
#### Parameters
id: string

#### Request Body
No request body

#### Response body
Status Code: 200

Example:
```
    {
        "accountNumber": "009922",
        "agencyNumber": "0080",
        "codeBank": "0040",
        "companyName": "bhub",
        "id": "49929993-a5ef-454e-9c72-566d9c4945f0"
    }
```

### DELETE /clients/bankAccounts/<id>
#### Parameters
id: string

#### Request Body
No request body

#### Response body
Status Code: 200

Example:
```
    Deleted with success
```

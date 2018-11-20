from enum import Enum


class Language(Enum):
    ENGLISH = 'en'
    SPANISH = 'es'
    PORTUGUESE = 'pt'


class Country(Enum):
    ARGENTINA = 'AR'
    BRAZIL = 'BR'
    COLOMBIA = 'CO'
    MEXICO = 'MX'
    PANAMA = 'PA'
    PERU = 'PE'
    CHILE = 'CL'


class Currency(Enum):
    ARGENTINA = 'ARS'
    BRAZIL = 'BRL'
    COLOMBIA = 'COP'
    MEXICO = 'MXN'
    USD = 'USD'
    PERU = 'PEN'
    CHILE = 'CLP'


class Franchise(Enum):
    VISA = 'VISA'
    MASTERCARD = 'MASTERCARD'
    AMEX = 'AMEX'
    DINERS = 'DINERS'
    ELO = 'ELO'
    NARANJA = 'NARANJA'
    SHOPPING = 'SHOPPING'
    CABAL = 'CABAL'
    ARGENCARD = 'ARGENCARD'
    CENCOSUD = 'CENCOSUD'
    HIPERCARD = 'HIPERCARD'
    CODENSA = 'CODENSA'
    VISA_DEBIT = 'VISA_DEBIT'


class DocumentType(Enum):
    CITIZENSHIP_CARD = 'CC'
    FOREIGN_CITIZENSHIP_CARD = 'CE'
    COMPANY = 'NIT'
    IDENTITY_CARD = 'TI'
    PASSPORT = 'PP'
    CLIENT_UNIQUE_IDENTIFIER = 'IDC'
    MOBILE_LINE = 'CEL'
    BIRTH_CERTIFICATE = 'RC'
    FOREIGN_IDENTIFICATION_DOCUMENT = 'DE'


class TransactionType(Enum):
    AUTHORIZATION = 'AUTHORIZATION'
    CAPTURE = 'CAPTURE'
    AUTHORIZATION_AND_CAPTURE = 'AUTHORIZATION_AND_CAPTURE'
    VOID = 'VOID'
    REFUND = 'REFUND'


class TransactionState(Enum):
    APPROVED = 'APPROVED'
    DECLINED = 'DECLINED'
    ERROR = 'ERROR'
    EXPIRED = 'EXPIRED'
    PENDING = 'PENDING'
    SUBMITTED = 'SUBMITTED'


class OrderStatus(Enum):
    NEW = 'NEW'
    IN_PROGRESS = 'IN_PROGRESS'
    AUTHORIZED = 'AUTHORIZED'
    CAPTURED = 'CAPTURED'
    CANCELLED = 'CANCELLED'
    DECLINED = 'DECLINED'
    REFUNDED = 'REFUNDED'


class PaymentCommand(Enum):
    PING = 'PING'
    SUBMIT_TRANSACTION = 'SUBMIT_TRANSACTION'
    GET_PAYMENT_METHODS = 'GET_PAYMENT_METHODS'
    GET_BANK_LIST = 'GET_BANK_LIST'

    CREATE_TOKEN = 'CREATE_TOKEN'
    GET_TOKENS = 'GET_TOKENS'
    REMOVE_TOKEN = 'REMOVE_TOKEN'


class QueryCommand(Enum):
    PING = 'PING'
    ORDER_DETAIL = 'ORDER_DETAIL'
    ORDER_DETAIL_REFERENCE_CODE = 'ORDER_DETAIL_REFERENCE_CODE'
    TRANSACTION_RESPONSE_DETAIL = 'TRANSACTION_RESPONSE_DETAIL'


class MessagePol(Enum):
    APPROVED = 'APPROVED'
    PAYMENT_NETWORK_REJECTED = 'PAYMENT_NETWORK_REJECTED'
    ENTITY_DECLINED = 'ENTITY_DECLINED'
    INSUFFICIENT_FUNDS = 'INSUFFICIENT_FUNDS'
    INVALID_CARD = 'INVALID_CARD'
    CONTACT_THE_ENTITY = 'CONTACT_THE_ENTITY'
    BANK_ACCOUNT_ACTIVATION_ERROR = 'BANK_ACCOUNT_ACTIVATION_ERROR'
    BANK_ACCOUNT_NOT_AUTHORIZED_FOR_AUTOMATIC_DEBIT = 'BANK_ACCOUNT_NOT_AUTHORIZED_FOR_AUTOMATIC_DEBIT'
    INVALID_AGENCY_BANK_ACCOUNT = 'INVALID_AGENCY_BANK_ACCOUNT'
    INVALID_BANK_ACCOUNT = 'INVALID_BANK_ACCOUNT'
    INVALID_BANK = 'INVALID_BANK'
    EXPIRED_CARD = 'EXPIRED_CARD'
    RESTRICTED_CARD = 'RESTRICTED_CARD'
    INVALID_EXPIRATION_DATE_OR_SECURITY_CODE = 'INVALID_EXPIRATION_DATE_OR_SECURITY_CODE'
    REPEAT_TRANSACTION = 'REPEAT_TRANSACTION'
    INVALID_TRANSACTION = 'INVALID_TRANSACTION'
    EXCEEDED_AMOUNT = 'EXCEEDED_AMOUNT'
    ABANDONED_TRANSACTION = 'ABANDONED_TRANSACTION'
    CREDIT_CARD_NOT_AUTHORIZED_FOR_INTERNET_TRANSACTIONS = 'CREDIT_CARD_NOT_AUTHORIZED_FOR_INTERNET_TRANSACTIONS'
    ANTIFRAUD_REJECTED = 'ANTIFRAUD_REJECTED'
    DIGITAL_CERTIFICATE_NOT_FOUND = 'DIGITAL_CERTIFICATE_NOT_FOUND'
    BANK_UNREACHABLE = 'BANK_UNREACHABLE'
    PAYMENT_NETWORK_NO_CONNECTION = 'PAYMENT_NETWORK_NO_CONNECTION'
    PAYMENT_NETWORK_NO_RESPONSE = 'PAYMENT_NETWORK_NO_RESPONSE'
    ENTITY_MESSAGING_ERROR = 'ENTITY_MESSAGING_ERROR'
    NOT_ACCEPTED_TRANSACTION = 'NOT_ACCEPTED_TRANSACTION'
    INTERNAL_PAYMENT_PROVIDER_ERROR = 'INTERNAL_PAYMENT_PROVIDER_ERROR'
    INACTIVE_PAYMENT_PROVIDER = 'INACTIVE_PAYMENT_PROVIDER'
    ERROR = 'ERROR'
    ERROR_CONVERTING_TRANSACTION_AMOUNTS = 'ERROR_CONVERTING_TRANSACTION_AMOUNTS'
    FIX_NOT_REQUIRED = 'FIX_NOT_REQUIRED'
    AUTOMATICALLY_FIXED_AND_SUCCESS_REVERSAL = 'AUTOMATICALLY_FIXED_AND_SUCCESS_REVERSAL'
    AUTOMATICALLY_FIXED_AND_UNSUCCESS_REVERSAL = 'AUTOMATICALLY_FIXED_AND_UNSUCCESS_REVERSAL'
    AUTOMATIC_FIXED_NOT_SUPPORTED = 'AUTOMATIC_FIXED_NOT_SUPPORTED'
    NOT_FIXED_FOR_ERROR_STATE = 'NOT_FIXED_FOR_ERROR_STATE'
    ERROR_FIXING_AND_REVERSING = 'ERROR_FIXING_AND_REVERSING'
    ERROR_FIXING_INCOMPLETE_DATA = 'ERROR_FIXING_INCOMPLETE_DATA'
    PAYMENT_NETWORK_BAD_RESPONSE = 'PAYMENT_NETWORK_BAD_RESPONSE'
    EXPIRED_TRANSACTION = 'EXPIRED_TRANSACTION'


class StatePol(Enum):
    APPROVED = '4'
    DECLINED = '6'
    EXPIRED = '5'

from pydantic import BaseModel, validator, Field, parse_obj_as
from datetime import date, datetime
from typing import Optional


class ProductionUnit(BaseModel):
    production_unit_number: int = None
    ######
    # Punit info
    ######
    start_date: date = None
    end_date: date = None


class AddressInfo(BaseModel):
    country_code: str = None
    free_text: str = None
    street_code: int = None
    commune_code: int = None
    commune_name: str = None
    street_name: str = None
    city_name: str = None
    postal_code: int = None
    postal_district: str = None
    street_no_from: int = None
    street_no_to: int = None
    address_id: str = None
    street_letter_from: str = None
    street_letter_to: str = None
    floor: str = None
    side_door: str = None
    co_name: str = None
    post_office_box: str = None


class TeleInfo(BaseModel):
    phone_number: str = None
    secret: bool = None


class EmailInfo(BaseModel):
    email: str = None
    secret: bool = None


class WebPageInfo(BaseModel):
    url: str = None
    secret: bool = None


class Company(BaseModel):
    vat_number: int
    registration_number: str = None
    industry_responsibility_code: int = None
    is_advertisement_protected: bool = None
    name: str = None
    alternative_name: str = None
    postal_address: AddressInfo = None
    phone_information: TeleInfo = None
    fax_information: TeleInfo = None
    secondary_phone_information: TeleInfo = None
    secondary_fax_information: TeleInfo = None
    email_info: EmailInfo = None
    webpage: WebPageInfo = None
    industry_code: str = None
    industry_text: str = None
    secondary_industry_code: str = None
    secondary_industry_text: str = None
    tertiary_industry_code: str = None
    tertiary_industry_text: str = None
    quaternary_industry_code: str = None
    quaternary_industry_text: str = None
    status_code: int = None
    status_text: str = None
    credit_information_code: int = None
    credit_information_text: str = None
    company_status: str = None
    form_of_business_code: int = None
    form_of_business_short_description: str = None
    form_of_business_long_description: str = None
    responsible_data_provider: str = None
    number_of_employees: int = None
    number_of_fte_employees: int = None
    start_date: date = None
    end_date: date = None



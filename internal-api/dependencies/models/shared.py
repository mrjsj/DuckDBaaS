from pydantic import BaseModel, Field
from datetime import date, datetime


class TeleInfo(BaseModel):
    phone_number: str = None
    secret: bool = None


class EmailInfo(BaseModel):
    email: str = None
    secret: bool = None


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


class Period(BaseModel):
    valid_from: date = Field(default=None, alias="gyldigFra", description="gyldigFra")
    valid_to: date = Field(default=None, alias="gyldigTil", description="gyldigTil")


class BasePeriodModel(BaseModel):
    period: Period = Field(default=None, alias="periode", description="periode")
    last_modified: datetime = Field(
        default=None, alias="sidstOpdateret", description="sidstOpdateret"
    )


class Name(BasePeriodModel):
    name: str = Field(default=None, alias="navn", description="navn")


class RegistrationNumber(BasePeriodModel):
    registration_number: str = Field(
        default=None, alias="regnummer", description="regnummer"
    )


class Value(BasePeriodModel):
    value: str = Field(default=None, alias="vaerdi", description="vaerdi")


class Attribute(BaseModel):
    sequence_number: int = Field(
        default=None, alias="sekvensnr", description="sekvensnr"
    )
    type: str = Field(default=None, alias="type", description="type")
    value_type: str = Field(default=None, alias="vaerditype", description="vaerditype")
    values: list[Value] = Field(default=None, alias="vaerdier", description="vaerdier")


class Status(BasePeriodModel):
    status_code: int = Field(default=None, alias="statuskode", description="statuskode")
    status_text: str = Field(
        default=None, alias="statustekst", description="statustekst"
    )
    credit_information_code: int = Field(
        default=None, alias="kreditoplysningkode", description="kreditoplysningkode"
    )
    credit_information_text: str = Field(
        default=None, alias="kreditoplysningtekst", description="kreditoplysningtekst"
    )


class CompanyStatus(BasePeriodModel):
    status: str = Field(default=None, alias="status", description="status")


class FormOfBusiness(BasePeriodModel):
    form_of_business_code: int = Field(
        default=None, alias="virksomhedsformkode", description="virksomhedsformkode"
    )
    short_description: str = Field(
        default=None, alias="kortBeskrivelse", description="kortBeskrivelse"
    )
    long_description: str = Field(
        default=None, alias="langBeskrivelse", description="langBeskrivelse"
    )
    responsible_data_provider: str = Field(
        default=None,
        alias="ansvarligDataleverandoer",
        description="ansvarligDataleverandoer",
    )


class BaseCompany(BaseModel):
    unit_number: int = Field(
        default=None, alias="enhedsNummer", description="enhedsNummer"
    )
    unit_type: str = Field(default=None, alias="enhedsType", description="enhedsType")
    is_registration_error: bool = Field(
        default=None, alias="fejlRegistreret", description="fejlRegistreret"
    )
    last_loaded: datetime = Field(
        default=None, alias="sidstIndlaest", description="sidstIndlaest"
    )
    last_modified: datetime = Field(
        default=None, alias="sidstOpdateret", description="sidstOpdateret"
    )
    vat_number: int = Field(default=None, alias="cvrNummer", description="cvrNummer")
    registration_numbers: list[RegistrationNumber] = Field(
        default=[], alias="regNummer", description="regNummer"
    )
    names: list[Name] = Field(default=None, alias="navne", description="navne")
    course_of_life: list[Period] = Field(
        default=None, alias="livsforloeb", description="livsforloeb"
    )
    statusses: list[Status] = Field(default=None, alias="status", description="status")
    company_statusses: list[CompanyStatus] = Field(
        default=None, alias="virksomhedsstatus", description="virksomhedsstatus"
    )
    form_of_business: list[FormOfBusiness] = Field(
        default=None, alias="virksomhedsform", description="virksomhedsform"
    )


class Member(BaseModel):
    attributes: list[Attribute] = Field(
        default=None, alias="attributter", description="attributter"
    )


class BaseOrganization(BaseModel):
    unit_number: int = Field(
        default=None,
        alias="enhedsNummerOrganisation",
        description="enhedsNummerOrganisation",
    )
    primary_type: str = Field(default=None, alias="hovedType", description="hovedType")
    names: list[Name] = Field(
        default=None, alias="organisationsNavn", description="organisationsNavn"
    )
    attributes: list[Attribute] = Field(
        default=None, alias="attributter", description="attributter"
    )
    members: list[Member] = Field(
        default=None, alias="medlemsData", description="medlemsData"
    )

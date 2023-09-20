from pydantic import BaseModel, Field
from datetime import datetime, date
from .shared import *
import random

class CompanySummaryRelation(BaseModel):
    company: BaseCompany = Field(
        default=None, alias="virksomhed", description="virksomhed"
    )
    organizations: list[BaseOrganization] = Field(
        default=[],
        alias="organisationer",
        description="organisationer",
    )


class ParticipantMetadata(BaseModel):
    current_address: AddressInfo = Field(
        default=None,
        alias="nyesteBeliggenhedsadresse",
        description="nyesteBeliggenhedsadresse",
    )
    current_contact_information: list[str] = Field(
        default=[],
        alias="nyesteKontaktoplysninger",
        description="nyesteKontaktoplysninger",
    )


class Participant(BaseModel):
    cvr_id: int = Field(
        default=None, alias="_id", description="_id"
    ) 
    business_key: int = Field(
        default=None, alias="forretningsnoegle", description="forretningsnoegle"
    )
    names: list[Name] = Field(default=[], alias="navne", description="navne")
    addresses: list[AddressInfo] = Field(
        default=[], alias="beliggenhedsadresse", description="beliggenhedsadresse"
    )
    is_address_protected: bool = Field(
        default=None, alias="adresseHemmelig", description="adresseHemmelig"
    )
    is_address_protected_exception: bool = Field(
        default=None,
        alias="adresseHemmeligUndtagelse",
        description="adresseHemmeligUndtagelse",
    )
    is_address_update_ceased: bool = Field(
        default=None,
        alias="adresseOpdateringOphoert",
        description="adresseOpdateringOphoert",
    )
    postal_addresses: list[AddressInfo] = Field(
        default=None, alias="postadresse", description="postadresse"
    )
    company_addresses: list[AddressInfo] = Field(
        default=[], alias="forretningsadresse", description="forretningsadresse"
    )
    phone_numbers: list[TeleInfo] = Field(
        default=[], alias="telefonNummer", description="telefonNummer"
    )
    telefax_numbers: list[TeleInfo] = Field(
        default=[], alias="telefaxNummer", description="telefaxNummer"
    )
    digital_mails: list[EmailInfo] = Field(
        default=[], alias="elektroniskPost", description="elektroniskPost"
    )
    position: str = Field(default=None, alias="stilling", description="stilling")
    status_code: int = Field(default=None, alias="statusKode", description="statusKode")
    company_summary_relations: list[CompanySummaryRelation] = Field(
        default=[],
        alias="virksomhedSummariskRelation",
        description="virksomhedSummariskRelation",
    )
    participant_metadata: ParticipantMetadata = Field(
        default=None,
        alias="deltagerpersonMetadata",
        description="deltagerpersonMetadata",
    )
    samt_id: int = Field(default=None, alias="samtid", description="samtid")
    is_data_access: bool = Field(
        default=None, alias="dataAdgang", description="dataAdgang"
    )
    unit_number: int = Field(
        default=None,
        alias="enhedsNummer",
        description="enhedsNummer",
    )
    unit_type: str = Field(default=None, alias="enhedstype", description="enhedstype")
    last_loaded: datetime = Field(
        default=None, alias="sidstIndlaest", description="sidstIndlaest"
    )
    last_modified: datetime = Field(
        default=None, alias="sidstOpdateret", description="sidstOpdateret"
    )
    is_error_during_load: bool = Field(
        default=None, alias="fejlVedIndlaesning", description="fejlVedIndlaesning"
    )
    closest_future_date: date = Field(
        default=None,
        alias="naermesteFremtidigeDato",
        description="naermesteFremtidigeDato",
    )
    error_description: str = Field(
        default=None, alias="fejlBeskrivelse", description="fejlBeskrivelse"
    )
    modified_by: str = Field(
        default=None, alias="virkningsAktoer", description="virkningsAktoer"
    )

    system_updated_at: datetime = Field(
        default=None, description="internal system calculated field"
    )

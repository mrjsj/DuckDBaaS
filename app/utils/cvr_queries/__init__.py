def get_should(endpoint: str, timestamp: str):
    SHOULD = {
        "virksomhed": [
            {
                "range": {
                    "Vrvirksomhed.deltagerRelation.deltager.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.virksomhedMetadata.nyesteBeliggenhedsadresse.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.deltagerRelation.deltager.navne.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.telefonNummer.sidstOpdateret": {"gte": f"{timestamp}"}
                }
            },
            {
                "range": {
                    "Vrvirksomhed.bibranche1.sidstOpdateret": {"gte": f"{timestamp}"}
                }
            },
            {
                "range": {
                    "Vrvirksomhed.livsforloeb.sidstOpdateret": {"gte": f"{timestamp}"}
                }
            },
            {
                "range": {
                    "Vrvirksomhed.virksomhedMetadata.nyesteHovedbranche.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.virksomhedMetadata.nyesteBibranche1.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.hjemmeside.sidstOpdateret": {"gte": f"{timestamp}"}
                }
            },
            {
                "range": {
                    "Vrvirksomhed.virksomhedMetadata.nyesteNavn.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.hovedbranche.sidstOpdateret": {"gte": f"{timestamp}"}
                }
            },
            {
                "range": {
                    "Vrvirksomhed.deltagerRelation.organisationer.medlemsData.attributter.vaerdier.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.elektroniskPost.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.virksomhedsform.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.deltagerRelation.organisationer.organisationsNavn.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {"range": {"Vrvirksomhed.navne.sidstOpdateret": {"gte": f"{timestamp}"}}},
            {
                "range": {
                    "Vrvirksomhed.beliggenhedsadresse.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.penheder.sidstOpdateret": {"gte": f"{timestamp}"}
                }
            },
            {
                "range": {
                    "Vrvirksomhed.deltagerRelation.deltager.beliggenhedsadresse.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.deltagerRelation.organisationer.attributter.vaerdier.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.beliggenhedsadresse.kommune.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrvirksomhed.virksomhedMetadata.nyesteVirksomhedsform.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {"range": {"Vrvirksomhed.sidstOpdateret": {"gte": f"{timestamp}"}}},
            {
                "range": {
                    "Vrvirksomhed.virksomhedMetadata.nyesteBeliggenhedsadresse.kommune.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
        ],
        "produktionsenhed": [
            {"range": {"VrproduktionsEnhed.sidstOpdateret": {"gte": f"{timestamp}"}}},
            {
                "range": {
                    "VrproduktionsEnhed.telefonNummer.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "VrproduktionsEnhed.produktionsEnhedMetadata.nyesteBeliggenhedsadresse.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "VrproduktionsEnhed.navne.sidstOpdateret": {"gte": f"{timestamp}"}
                }
            },
            {
                "range": {
                    "VrproduktionsEnhed.virksomhedsrelation.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "VrproduktionsEnhed.elektroniskPost.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "VrproduktionsEnhed.beliggenhedsadresse.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "VrproduktionsEnhed.livsforloeb.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "VrproduktionsEnhed.hovedbranche.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "VrproduktionsEnhed.beliggenhedsadresse.kommune.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "VrproduktionsEnhed.produktionsEnhedMetadata.nyesteBeliggenhedsadresse.kommune.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "VrproduktionsEnhed.produktionsEnhedMetadata.nyesteHovedbranche.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "VrproduktionsEnhed.produktionsEnhedMetadata.nyesteNavn.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
        ],
        "deltager": [
            {"range": {"Vrdeltagerperson.sidstOpdateret": {"gte": f"{timestamp}"}}},
            {
                "range": {
                    "Vrdeltagerperson.virksomhedSummariskRelation.virksomhed.navne.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrdeltagerperson.virksomhedSummariskRelation.virksomhed.livsforloeb.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrdeltagerperson.navne.sidstOpdateret": {"gte": f"{timestamp}"}
                }
            },
            {
                "range": {
                    "Vrdeltagerperson.virksomhedSummariskRelation.organisationer.medlemsData.attributter.vaerdier.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrdeltagerperson.virksomhedSummariskRelation.virksomhed.virksomhedsform.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrdeltagerperson.virksomhedSummariskRelation.virksomhed.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrdeltagerperson.attributter.vaerdier.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrdeltagerperson.virksomhedSummariskRelation.organisationer.attributter.vaerdier.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrdeltagerperson.deltagerpersonMetadata.nyesteBeliggenhedsadresse.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrdeltagerperson.beliggenhedsadresse.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrdeltagerperson.virksomhedSummariskRelation.virksomhed.virksomhedsstatus.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
            {
                "range": {
                    "Vrdeltagerperson.virksomhedSummariskRelation.organisationer.organisationsNavn.sidstOpdateret": {
                        "gte": f"{timestamp}"
                    }
                }
            },
        ],
    }

    return SHOULD.get(endpoint)

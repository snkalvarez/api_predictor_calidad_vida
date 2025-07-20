swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API de Inventario",
        "description": "API RESTful para manejo de inventario. Incluye operaciones CRUD.",
        "version": "1.0.0",
        "termsOfService": "https://tusitio.com/terminos",
        "contact": {
            "name": "Julio Cesar Alvarez Cuaces & Juan Carlos Ruales",
            "email": "lcalvarez@unicauca.edu.co"
        },
        "license": {
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT"
        }
    },
    "basePath": "/",
    "schemes": ["http"],
    "definitions": {
        "Preguntas": {
            "type": "object",
            "required": ["mother_education_level","father_education_level","life_satisfaction_level","job_satisfaction_level","per_capita_income","expenditure_unit_monthly_income","household_size","mother_lives_household","father_lives_household","current_age","cognitive_ability","income_satisfaction_level","life_worthwhileness","hand_grip_ability","mobility_ability","vision_ability","speech_ability","hearing_ability","has_chronic_disease","general_health_status","other_health_services","student_health_insurance","hospitalization_surgery_policy","eps_complementary_health_plan","private_health_insurance","health_insurance_affiliation","gender","self_care_ability","health_issue_last_30_days"],
            "properties": {
                "mother_education_level":{
                    "type": "string",
                    "description": "el nivel educativo alcanzado por la madre puede tomar estos valores (Ninguno,NSNC,PrimComp,PrimIncomp,SecComp,SecIncomp,TecComp,TecIncomp,UnivComp,UnivIncomp)",
                    "example": "PrimIncomp",
                },                
                "father_education_level":{
                    "type": "string",
                    "description": "el nivel educativo alcanzado por la madre puede tomar estos valores (Ninguno,NSNC,PrimComp,PrimIncomp,SecComp,SecIncomp,TecComp,TecIncomp,UnivComp,UnivIncomp)",
                    "example": "SecIncomp",
                },
                "life_satisfaction_level":{
                    "type": "integer",
                    "description": "nivel de satisfacción con la vida, puede tomar valores entre 0 y 10",
                    "example": 3,
                },
                "job_satisfaction_level":{
                    "type": "integer",
                    "description": "nivel de satisfacción con el trabajo, puede tomar valores entre 0 y 10",
                    "example": 4,
                },
                "per_capita_income":{
                    "type": "double",
                    "description": "ingreso per cápita",
                    "example": 142083.333,
                },
                "expenditure_unit_monthly_income":{
                    "type": "double",
                    "description": "ingreso mensual por unidad de gasto",
                    "example": 2424166.667,
                },
                "household_size":{
                    "type": "integer",
                    "description": "cantidad de personas que viven en el hogar",
                    "example": 4,
                },
                "mother_lives_household":{
                    "type": "string",
                    "description": "la madre vive en el hogar puede tomar estos valores (Si,No,Fallecida)",
                    "example": "No",
                },
                "father_lives_household":{
                    "type": "string",
                    "description": "el padre vive en el hogar puede tomar estos valores (Si,No,Fallecido)",
                    "example": "Si",
                },
                "current_age":{
                    "type": "integer",
                    "description": "edad actual del encuestado",
                    "example": 25,
                },
                "cognitive_ability":{
                    "type": "string",
                    "description": "capacidad cognitiva del encuestado puede tomar estos valores (SinDif,AlgoDif,MuchaDif,NoPuede)",
                    "example": "SinDif",
                },
                "income_satisfaction_level":{
                    "type": "integer",
                    "description": "nivel de satisfacción con el ingreso, puede tomar valores entre 0 y 10",
                    "example": 7,
                },
                "life_worthwhileness":{
                    "type": "integer",
                    "description": "nivel de satisfacción con la vida, puede tomar valores entre 0 y 10",
                    "example": 10,
                },
                "hand_grip_ability":{
                    "type": "string",
                    "description": "capacidad de agarre de la mano puede tomar estos valores (SinDif,AlgoDif,MuchaDif,NoPuede)",
                    "example": "SinDif",
                },
                "mobility_ability":{
                    "type": "string",
                    "description": "capacidad de movilidad puede tomar estos valores (SinDif,AlgoDif,MuchaDif,NoPuede)",
                    "example": "SinDif",
                },
                "vision_ability":{
                    "type": "string",
                    "description": "capacidad visual puede tomar estos valores (SinDif,AlgoDif,MuchaDif,NoPuede)",
                    "example": "SinDif",
                },
                "speech_ability":{
                    "type": "string",
                    "description": "capacidad de habla puede tomar estos valores (SinDif,AlgoDif,MuchaDif,NoPuede)",
                    "example": "SinDif",
                },
                "hearing_ability":{
                    "type": "string",
                    "description": "capacidad auditiva puede tomar estos valores (SinDif,AlgoDif,MuchaDif,NoPuede)",
                    "example": "SinDif",
                },
                "has_chronic_disease":{
                    "type": "string",
                    "description": "si el encuestado tiene alguna enfermedad crónica puede tomar estos valores (No,Si)",
                    "example": "No",
                },
                "general_health_status":{
                    "type": "string",
                    "description": "estado de salud general puede tomar estos valores (Bueno,Malo,MuyBuen,Regular)",
                    "example": "MuyBuen",
                },
                "other_health_services":{
                  "type": "string",
                  "description": "si el encuestado tiene acceso a otros servicios de salud puede tomar estos valores (No,Si)",
                  "example": "No",
                },
                "student_health_insurance":{
                  "type": "string",
                  "description": "si el encuestado tiene seguro de salud estudiantil puede tomar estos valores (No,Si)",
                  "example": "No",
                },
                "hospitalization_surgery_policy":{
                  "type": "string",
                  "description": "si el encuestado tiene póliza de hospitalización o cirugía puede tomar estos valores (No,Si)",
                  "example": "No",
                },
                "eps_complementary_health_plan":{
                  "type": "string",
                  "description": "si el encuestado tiene plan de salud complementario a la EPS puede tomar estos valores (No,Si)",
                  "example": "No",
                },
                "private_health_insurance":{
                  "type": "string",
                  "description": "si el encuestado tiene seguro de salud privado puede tomar estos valores (No,Si)",
                  "example": "No",
                },
                "health_insurance_affiliation":{
                  "type": "string",
                  "description": "si el encuestado tiene afiliación a un seguro de salud puede tomar estos valores (No,NSNC,Si)",
                  "example": "Si",
                },
                "gender":{
                  "type": "string",
                  "description": "género del encuestado puede tomar estos valores (Masc,Fem)",
                  "example": "Fem",
                },
                "self_care_ability":{
                  "type": "string",
                  "description": "capacidad de autocuidado puede tomar estos valores (SinDif,AlgoDif,MuchaDif,NoPuede)",
                  "example": "SinDif",
                },
                "health_issue_last_30_days":{
                  "type": "string",
                  "description": "si el encuestado ha tenido problemas de salud en los últimos 30 días puede tomar estos valores (No,Si)",
                  "example": "No",
                }
            }
        }
    }
}
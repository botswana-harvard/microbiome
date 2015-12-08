from edc_constants.constants import (
    NOT_APPLICABLE, UNKNOWN, OTHER, UNSCHEDULED, SCHEDULED, MISSED_VISIT, LOST_VISIT,
    OFF_STUDY, DEATH_VISIT)

from .constants import NO_MODIFICATIONS, START, BREASTFEED_ONLY


VISIT_INFO_SOURCE = [
    ('participant', 'Clinic visit with participant'),
    ('other_contact', 'Other contact with participant (for example telephone call)'),
    ('other_doctor', 'Contact with external health care provider/medical doctor'),
    ('family', 'Contact with family or designated person who can provide information'),
    ('chart', 'Hospital chart or other medical record'),
    (OTHER, 'Other')]

# DONT CHANGE THESE !!
VISIT_REASON = [
    (SCHEDULED, 'Scheduled visit/contact'),
    (MISSED_VISIT, 'Missed Scheduled visit'),
    (UNSCHEDULED, 'Unscheduled visit at which lab samples or data are being submitted'),
    (LOST_VISIT, 'Lost to follow-up (use only when taking subject off study)'),
    (DEATH_VISIT, 'Death'),
    (OFF_STUDY, 'Subject has completed the study')]

VISIT_UNSCHEDULED_REASON = (
    ('Routine oncology', 'Routine oncology clinic visit'),
    ('Ill oncology', 'Ill oncology clinic visit'),
    ('Patient called', 'Patient called to come for visit'),
    (OTHER, 'Other, specify:'),
)

HAART_DURING_PREG = (
    ('Atripla', 'Atripla'),
    ('Truvada-Efavirenz ', 'Truvada-Efavirenz '),
    ('Tenofovir-Emtricitibine-Efavirenz', 'Tenofovir-Emtricitibine-Efavirenz'),
    ('Truvad-Lamivudine-Efavirenz', 'Truvad-Lamivudine-Efavirenz'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

PREG_DELIVERED_CHOICE = (
    ('pregnant', 'Pregnant'),
    ('delivered ', 'Delivered '),
)

BIRTH_TYPE = (
    ('vaginal ', 'vaginal'),
    ('cesarean ', 'cesarean'),
)

ARV_INTERRUPTION_REASON = (
    ('TOXICITY', 'Toxicity'),
    ('NO_DRUGS', 'No drugs available'),
    ('NO_REFILL', 'Didn\'t get to clinic for refill'),
    ('FORGOT', 'Mother forgot to take the ARVs'),
    (OTHER, 'Other'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

AUTOPSY_SOURCE = (
    ('mother', 'Mother of infant'),
    ('family_mem', 'Other family member'),
    ('hlth_prof', 'Health Professional who cared for the infant'),
    ('med_rec', 'Medical records'),
    (OTHER, 'Other'),
)

AUTOPSY_SIGNS = (
    ('fever', 'Fever'),
    ('poor_feeding', 'Poor feeding'),
    ('weight_loss', 'Weight loss'),
    ('weakness', 'Weakness'),
    ('stiff_neck', 'Stiff Neck'),
    ('unusual_sleepiness', 'Unusual sleepiness'),
    ('convulsions', 'Convulsions'),
    ('bleeding', 'Bleeding'),
    ('cough', 'Cough'),
    ('diffic_breathing', 'Difficulty breathing'),
    ('swollen_stomach', 'Swollen stomach'),
    ('Vomiting', 'Vomiting'),
    ('diarrhea', 'Diarrhea'),
    ('blood_pus_stool', 'Blood or pus in stool'),
    ('rash_body', 'Rash on body'),
    ('rash_mouth', 'Rash or sores in mouth'),
    ('yellow_eyes_skin', 'Yellow eyes or skin'),
    ('accident', 'Accident'),
    ('infection_genitals', 'Local infection (genitals)'),
    ('infect_other_area', 'Local infection (other than genitals'),
)

FEEDING_CHOICES = (
    (BREASTFEED_ONLY, 'Breastfeed only'),
    ('Formula feeding only', 'Formula feeding only'),
    ('Both breastfeeding and formula feeding', 'Both breastfeeding and formula feeding'),
    ('Medical complications: Infant did not feed', 'Medical complications: Infant did not feed'),
)

CARDIOVASCULAR_DISORDER = (
    ('None', 'None'),
    ('Truncus arteriosus', 'Truncus arteriosus'),
    ('Atrial septal defect', 'Atrial septal defect'),
    ('Ventricula septal defect', 'Ventricula septal defect'),
    ('Atrioventricular canal', 'Atrioventricular canal'),
    ('Complete transposition of the great vessels (without VSD)',
     'Complete transposition of the great vessels (without VSD)'),
    ('Complete transposition of the great vessels (with VSD)',
     'Complete transposition of the great vessels (with VSD)'),
    ('Tetralogy of Fallot', 'Tetralogy of Fallot'),
    ('Pulmonary valve stenosis or atresia', 'Pulmonary valve stenosis or atresia'),
    ('Tricuspid valve stenosis or atresia', 'Tricuspid valve stenosis or atresia'),
    ('Mitral valve stenosis or atresia', 'Mitral valve stenosis or atresia'),
    ('Hypoplastic left ventricle', 'Hypoplastic left ventricle'),
    ('Hypoplastic right ventricle', 'Hypoplastic right ventricle'),
    ('Congenital cardiomyopath (do not code if only isolated cardiomegaly)',
     'Congenital cardiomyopath (do not code if only isolated cardiomegaly)'),
    ('Coarclation of the aorta', 'Coarclation of the aorta'),
    ('Total anomalous pulmonary venous return', 'Total anomalous pulmonary venous return'),
    ('Arteriovenous malformation, specify site', 'Arteriovenous malformation, specify site'),
    ('Patent ductous arteriosus (persisting >6 weeks of age)',
     'Patent ductous arteriosus (persisting >6 weeks of age)'),
    (OTHER, 'Other cardiovascular malformation, specify'),
)

CLEFT_DISORDER = (
    ('None', 'None'),
    ('Cleft lip without cleft palate', 'Cleft lip without cleft palate'),
    ('Cleft palate without cleft lip', 'Cleft palate without cleft lip'),
    ('Cleft lip and palate', 'Cleft lip and palate'),
    ('Cleft uvula', 'Cleft uvula'),
)

CNS_ABNORMALITIES = (
    ('None', 'None'),
    ('Anencephaly', 'Anencephaly'),
    ('Encephaloceis', 'Encephaloceis'),
    ('Spina bifida, open', 'Spina bifida, open'),
    ('Spina bifida, closed', 'Spina bifida, closed'),
    ('Holoprosencephaly', 'Holoprosencephaly'),
    ('Isolated hydroencephaly (not associated with spina bifida)',
     'Isolated hydroencephaly (not associated with spina bifida)'),
    ('Other CNS defect, specify', 'Other CNS defect, specify'),
)

COWS_MILK = (
    ('boiled', '1. Boiled from cow'),
    ('unboiled', '2. Unboiled from cow'),
    ('store', '3. From store'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

CTX_PLACEBO_STATUS = (
    ('No modification', 'No modifications made to CTX/Placebo since the last scheduled visit or today'),
    ('Starting CTX/Placebo today', 'Starting CTX/Placebo today or since the last scheduled visit'),
    ('Permanently discontinued', 'Permanently discontinued CTX/Placebo at or before last scheduled visit'),
    ('Never started', 'Never started CTX/Placebo'),
    ('Change in CTX/Placebo since the last scheduled visit or today',
     ('Change in CTX/Placebo since the last scheduled visit or today (dose modification, '
      'permanent discontinuation, temporary hold, resumption / initiation after temporary hold)')),
)

DX_INFANT = (
    ('Pneumonia, suspected (no CXR or microbiologic confirmation)',
     'Pneumonia, suspected (no CXR or microbiologic confirmation)'),
    ('Pneumonia, CXR confirmed, no bacterial pathogen',
     'Pneumonia, CXR confirmed, no bacterial pathogen'),
    ('Pneumonia, CXR confirmed, bacterial pathogen isolated (specify pathogen)',
     'Pneumonia, CXR confirmed, bacterial pathogen isolated (specify pathogen)'),
    ('Pulmonary TB, suspected(no CXR or microbiologic confirmation)',
     'Pulmonary TB, suspected(no CXR or microbiologic confirmation)'),
    ('Pulmonary TB, CXR-confirmed (no microbiologic confirmation)',
     'Pulmonary TB, CXR-confirmed (no microbiologic confirmation)'),
    ('Pulmonary TB, smear and/or culture positive',
     'Pulmonary TB, smear and/or culture positive'),
    ('Extrapulmonary TB,suspected (no CXR or microbiologic confirmation)',
     'Extrapulmonary TB,suspected (no CXR or microbiologic confirmation)'),
    ('Bronchiolitis (not bronchitis)', 'Bronchiolitis (not bronchitis)'),
    ('Hepatitis:Drug related', 'Hepatitis:Drug related (report for Grades 2,3,4)'),
    ('Hepatitis:Traditional medication related',
     'Hepatitis:Traditional medication related'),
    ('Hepatitis:Hepatitis A', 'Hepatitis:Hepatitis A'),
    ('Hepatitis:Hepatitis B', 'Hepatitis:Hepatitis B'),
    ('Hepatitis:Other/Unknown', 'Hepatitis:Other/Unknown'),
    ('Sepsis,unspecified', 'Sepsis,unspecified'),
    ('Sepsis,pathogen specified', 'Sepsis,pathogen specified'),
    ('Meningitis,unspecified', 'Meningitis,unspecified'),
    ('Meningitis pathogen specified', 'Meningitis pathogen specified'),
    ('Otitis media', 'Otitis media'),
    ('Appendicitis', 'Appendicitis'),
    ('Cholecystitis/cholanangitis', 'Cholecystitis/cholanangitis'),
    ('Pancreatitis', 'Pancreatitis'),
    ('Acute Renal Failure',
     'Acute Renal Failure (Record highest creatinine level if creatine tested outside of the study) '),
    ('Anemia', 'Anemia(Only report grade 3 or 4 anemia based on a lab value drawn outside the study'),
    ('Rash', 'Rash (report for Grades 2,3,4)'),
    ('Trauma/accident', 'Trauma/accident'),
    (
        ('Other abnormallaboratory tests(other than tests listed above '
         'or tests done as part of this study), specify test and result'),
        ('Other abnormallaboratory tests(other than tests listed above or '
         'tests done as part of this study),specify test and result')
    ),
    ('New congenital abnormality not previously identified?,specify',
     'New congenital abnormality not previously identified?,specify and complete "Congenital Anomaly"form'),
    ('Other serious (grade 3 or 4)infection(not listed above),specify',
     'Other serious (grade 3 or 4)infection(not listed above),specify'),
    ('Other serious (grade 3 or 4) non-infectious(not listed above),specify',
     'Other serious (grade 3 or 4)non-infectious(not listed above),specify'),

)

DX_MATERNAL = (
    ('Pneumonia suspected, no CXR or microbiologic confirmation',
     'Pneumonia suspected, no CXR or microbiologic confirmation'),
    ('Pneumonia, CXR confirmed, no bacterial pathogen', 'Pneumonia, CXR confirmed, no bacterial pathogen'),
    ('Pneumonia, CXR confirmed, bacterial pathogen isolated (specify pathogen)',
     'Pneumonia, CXR confirmed, bacterial pathogen isolated (specify pathogen)'),
    ('Pulmonary TB, suspected(no CXR or microbiologic confirmation)',
     'Pulmonary TB, suspected(no CXR or microbiologic confirmation)'),
    ('Pulmonary TB, CXR-confirmed (no microbiologic confirmation)',
     'Pulmonary TB, CXR-confirmed (no microbiologic confirmation)'),
    ('Pulmonary TB, smear and/or culture positive', 'Pulmonary TB, smear and/or culture positive'),
    ('Extrapulmonary TB,suspected (no CXR or microbiologic confirmation) ',
     'Extrapulmonary TB,suspected (no CXR or microbiologic confirmation) '),
    ('Extrapulmonary TB, smear and/or culture positive', 'Extrapulmonary TB, smear and/or culture positive'),
    (
        ('Acute diarrheal illness (bloody diarrhean OR increase of at least 7 stools per day '
         'OR life threatening for less than 14 days'),
        ('Acute diarrheal illness (bloody diarrhean OR increase of at least 7 stools per day '
         'OR life threatening for less than 14 days')),
    ('Chronic diarrheal illness (as above but for 14 days or longer) ',
     'Chronic diarrheal illness (as above but for 14 days or longer) '),
    ('Acute Hepatitis in this pregnancy: Drug related ', 'Acute Hepatitis in this pregnancy: Drug related '),
    ('Acute Hepatitis in this pregnancy:Traditional medication related',
     'Acute Hepatitis in this pregnancy:Traditional medication related'),
    ('Acute Hepatitis in this pregnancy:Fatty liver disease',
     'Acute Hepatitis in this pregnancy:Fatty liver disease'),
    ('Acute Hepatitis in this pregnancy:Hepatitis A', 'Acute Hepatitis in this pregnancy:Hepatitis A'),
    ('Acute Hepatitis in this pregnancy:Hepatitis B ', 'Acute Hepatitis in this pregnancy:Hepatitis B'),
    ('Acute Hepatitis in this pregnancy:Alcoholic', 'Acute Hepatitis in this pregnancy:Alcoholic'),
    ('Acute Hepatitis in this pregnancy:Other/Unkown', 'Acute Hepatitis in this pregnancy:Other/Unkown'),
    ('Sepsis, unspecified', 'Sepsis, unspecified'),
    ('Sepsis, pathogen specified', 'Sepsis, pathogen specified'),
    ('Meningitis, unspecified', 'Meningitis, unspecified'),
    ('Meningitis, pathogen specified', 'Meningitis, pathogen specified'),
    ('Appendicitis', 'Appendicitis'),
    ('Cholecystitis/cholanangitis', 'Cholecystitis/cholanangitis'),
    ('Pancreatitis', 'Pancreatitis'),
    ('Acute Renal failure',
     'Acute Renal failure (Record highest creatinine level if tested outside of the study)'),
    ('Anemia', 'Anemia (Only report grade 3 or 4 anemia based on the lab value drawn outside the study)'),
    ('Pregnancy/peripartum cardiomyopathy or CHF ', 'Pregnancy/peripartum cardiomyopathy or CHF '),
    ('Drug rash on HAART', 'Drug rash on HAART'),
    ('Trauma/Accident', 'Trauma/Accident'),
    ('Other serious (grade 3 or 4) infection, specify',
     'Other serious (grade 3 or 4) infection(not listed above), specify'),
    ('Other serious (grade 3 or 4) non-infectious diagnosis, specify',
     'Other serious (grade 3 or 4) non-infectious diagnosis(not listed above), specify'),
)

DRUG_RELATIONSHIP = (
    ('Not related', 'Not related'),
    ('Probably not related', 'Probably not related'),
    ('Possibly related', 'Possibly related'),
    ('Probably related', 'Probably related'),
    ('Definitely related', 'Definitely related'),
)

FACIAL_DEFECT = (
    ('None', 'None'),
    ('Anophthalmia/micro-opthalmia', 'Anophthalmia/micro-opthalmia'),
    ('Cataracts', 'Cataracts'),
    ('Coloboma', 'Coloboma'),
    ('OTHER eye abnormality', 'Other eye abnormality, specify'),
    ('Absence of ear', 'Absence of ear'),
    ('Absence of auditory canal', 'Absence of auditory canal'),
    ('Congenital deafness', 'Congenital deafness'),
    ('Microtia', 'Microtia'),
    ('OTHER ear anomaly', 'Other ear anomaly, specify'),
    ('Brachial cleft cyst, sinus or pit', 'Brachial cleft cyst, sinus or pit'),
    ('OTHER facial malformation', 'Other facial malformation, specify'),
)

FEM_GENITAL_ANOMALY = (
    ('None', 'None'),
    ('Ambinguous genitalia, female', 'Ambinguous genitalia, female'),
    ('Vaginal agenesis', 'Vaginal agenesis'),
    ('Absent or streak ovary', 'Absent or streak ovary'),
    ('Uterine anomaly', 'Uterine anomaly'),
    (OTHER, 'Other ovarian, fallopian, uterine, cervical, vaginal, or vulvar abnormality'),
)

INFO_PROVIDER = (
    ('MOTHER', 'Mother'),
    ('GRANDMOTHER', 'Grandmother'),
    ('FATHER', 'Father'),
    ('GRANDFATHER', 'Grandfather'),
    ('SIBLING', 'Sibling'),
    (OTHER, 'Other'),
)

INFANT_OFF_DRUG_REASON = (
    ('completed protocol', '1. Completion of protocol-required period of study treatment'),
    ('off-study', '2. Participant going off-study for any reason, including death or lost to follow-up'),
    (
        'toxicity',
        ('3. At Investigator\'s discretion, due to persistent toxicity '
         '(confirmed or suspected to be possibly related to study drug)')),
    ('caregiver', '4. Participant\'s mother/caregiver no longer wants child to receive study drug'),
    ('hiv infected', '5. Child is HIV- infected (Open-label CTX indicated)'),
    (OTHER, '9. Other'),
)

INFANT_VISIT_STUDY_STATUS = (
    ('onstudy', 'On study'),
    ('offstudy', 'Off study-no further follow-up (including death); use only for last study contact'),
)


OFF_STUDY_REASON = [
    ('gestations less than 37', ' Gestational age is less than 37 weeks'),
    ('moved', ' Subject will be moving out of study area or unable to stay in study area'),
    ('lost_no_contact', ' Lost to follow-up, unable to locate'),
    ('lost_contacted', ' Lost to follow-up, contacted but did not come to study clinic'),
    ('withdrew_by_mother', ' Mother changed mind and withdrew consent'),
    ('withdrew_by_father',
     ' Father of baby did not want infant to participate and participant withdrew consent'),
    ('withdrew_by_family',
     ' Other family member did not want mother/infant to participate and participant withdrew consent'),
    ('hiv_pos', ' Infant found to be HIV-infected'),
    ('complete',
        (' Completion of protocol required period of time for observation '
         '(see Study Protocol for definition of Completion.) [skip to end of form]')),
    ('death',
        (' Participant death (complete the DEATH REPORT FORM AF005) '
         '(For EAE Reporting requirements see EAE Reporting Manual)')),
    (OTHER, ' Other'),
]

LOWER_GASTROINTESTINAL_ABNORMALITY = (
    ('None', 'None'),
    ('Duodenal atresia, stenosis, or absence', 'Duodenal atresia, stenosis, or absence'),
    ('Jejunal atresis, stenosis, or absence', 'Jejunal atresis, stenosis, or absence'),
    ('Ileal atresia, stenosis, or absence', 'Ileal atresia, stenosis, or absence'),
    ('Atresia, stenosis, or absence of large intestine, rectum, or anus',
     'Atresia, stenosis, or absence of large intestine, rectum, or anus'),
    ('Hirschsprung disease', 'Hirschsprung disease'),
    ('OTHER megacolon', 'Other megacolon'),
    ('Liver, pancreas, or gall bladder defect, specify', 'Liver, pancreas, or gall bladder defect, specify'),
    ('Diaphramtic hernia', 'Diaphramtic hernia'),
    ('OTHER GI anomaly', 'Other GI anomaly, specify'),
)

MALE_GENITAL_ANOMALY = (
    ('None', 'None'),
    ('Hypospadias, specify degree', 'Hypospadias, specify degree'),
    ('Chordee', 'Chordee'),
    ('Ambiguous genitalia, male', 'Ambiguous genitalia, male'),
    ('Undescended testis', 'Undescended testis'),
    (OTHER, 'Other male genital abnormality, specify'),
)

BREAST_CHOICE = (
    ('right breast', 'Right breast only'),
    ('left breast', 'Left breast only'),
    ('both breasts', 'Both breasts'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

MEDICATIONS = (
    ('Acyclovir', 'Acyclovir'),
    ('Albuterol', 'Albuterol'),
    ('Albendazol', 'Albendazol'),
    ('Aminophylline', 'Aminophylline'),
    ('Amoxicillin', 'Amoxicillin'),
    ('Ampicillin', 'Ampicillin'),
    ('Antibiotic,unknown(specify 1V or oral)', 'Antibiotic,unknown(specify 1V or oral)'),
    ('Azithromycin', 'Azithromycin'),
    ('Carbamazepine', 'Carbamazepine'),
    ('Ceftriaxone', 'Ceftriaxone'),
    ('Cotrimoxazole (trimethoprim/sulfamethoxazole)', 'Cotrimoxazole (trimethoprim/sulfamethoxazole)'),
    ('Cefaclor,cefixime,ceftizoxime,ceftraxone', 'Cefaclor,cefixime,ceftizoxime,ceftraxone'),
    ('Chloramphenicol', 'Chloramphenicol'),
    ('Ciprofloxacin', 'Ciprofloxacin'),
    ('Clarithromycin', 'Clarithromycin'),
    ('Cloxacillin', 'Cloxacillin'),
    ('Doxycycline', 'Doxycycline'),
    ('Dexamethasone', 'Dexamethasone'),
    ('Diazepam', 'Diazepam'),
    ('Erythromycin', 'Erythromycin'),
    ('Ethambutol', 'Ethambutol'),
    ('Ferrous sulfate', 'Ferrous sulfate'),
    ('Fuconazole', 'Fuconazole'),
    ('Foscarnate', 'Foscarnate'),
    ('Ganciclovir', 'Ganciclovir'),
    ('Gentamicin', 'Gentamicin'),
    ('Hydrocortisone', 'Hydrocortisone'),
    ('Insuline', 'Insuline'),
    ('Isoniazid', 'Isoniazid'),
    ('Ketoconazole', 'Ketoconazole'),
    ('Mebendazole', 'Mebendazole'),
    ('Metronidazole', 'Metronidazole'),
    ('Methylprednisolone', 'Methylprednisolone'),
    ('Nalidixic acid', 'Nalidixic acid'),
    ('Norfloxacin,Ofloxacin', 'Norfloxacin,Ofloxacin'),
    ('Pentamidine', 'Pentamidine'),
    ('Pyridoxine', 'Pyridoxine'),
    ('Phenytoin', 'Phenytoin'),
    ('Prednisolone', 'Prednisolone'),
    ('Pyrazinamide', 'Pyrazinamide'),
    ('Pyrimethamine', 'Pyrimethamine'),
    ('Quinidine', 'Quinidine'),
    ('Red blood cell transfusion', 'Red blood cell transfusion'),
    ('Rifampicin', 'Rifampicin'),
    ('Salbutamol', 'Salbutamol'),
    ('Streptomycin', 'Streptomycin'),
    ('Sulfadiazine', 'Sulfadiazine'),
    ('Terbinafine', 'Terbinafine'),
    ('Tetracycline', 'Tetracycline'),
    ('Theophylline', 'Theophylline'),
    ('Vancomycin', 'Vancomycin'),
    ('Vitamins(iron,B12,Folate)', 'Vitamins(iron,B12,Folate)'),
    ('Traditional medication', 'Traditional Medications'),
    (OTHER, 'Other, specify ...')
)

MOUTH_UP_GASTROINT_DISORDER = (
    ('None', 'None'),
    ('Aglossia', 'Aglossia'),
    ('Macroglossia', 'Macroglossia'),
    ('OTHER mouth, lip, or tongue', 'Other mouth, lip, or tongue anomaly, specify'),
    ('Esophageal atresia', 'Esophageal atresia'),
    ('Tracheoesphageal fistula', 'Tracheoesphageal fistula'),
    ('Esophageal web', 'Esophageal web'),
    ('Pyloric stenosis', 'Pyloric stenosis'),
    ('OTHER esophageal or stomach', 'Other esophageal or stomach abnormality, specify'),
)

MUSCULOSKELETAL_ABNORMALITY = (
    ('None', 'None'),
    ('Craniosynostosis', 'Craniosynostosis'),
    ('Torticollis', 'Torticollis'),
    ('Congenital scoliosis, lordosis', 'Congenital scoliosis, lordosis'),
    ('Congenital dislocation of hip', 'Congenital dislocation of hip'),
    ('Talipes equinovarus (club feet excluding metatarsus varus)',
     'Talipes equinovarus (club feet excluding metatarsus varus)'),
    ('Funnel chest or pigeon chest (pectus excavatum or carinaturn)',
     'Funnel chest or pigeon chest (pectus excavatum or carinaturn)'),
    ('Polydactyly', 'Polydactyly'),
    ('Syndactyly', 'Syndactyly'),
    ('Other hand malformation, specify', 'Other hand malformation, specify'),
    ('Webbed fingers or toes', 'Webbed fingers or toes'),
    ('Upper limb reduction defect, specify', 'Upper limb reduction defect, specify'),
    ('Lower limb reduction defect, specify', 'Lower limb reduction defect, specify'),
    ('Other limb defect, specify', 'Other limb defect, specify'),
    ('Other skull abnormality, specify', 'Other skull abnormality, specify'),
    ('Anthrogryposis', 'Anthrogryposis'),
    ('Vertebral or rib abnormalities, specify', 'Vertebral or rib abnormalities, specify'),
    ('Osteogenesis imperfecta', 'Osteogenesis imperfecta'),
    ('Dwarfing syndrome, specify', 'Dwarfing syndrome, specify'),
    ('Congenital diaphramatic hernia', 'Congenital diaphramatic hernia'),
    ('Omphalocele', 'Omphalocele'),
    ('Gastroschisis', 'Gastroschisis'),
    (OTHER, 'Other muscular or skeletal abnormality or syndrome, specify'),
)

OTHER_DEFECT = (
    ('None', 'None'),
    (OTHER, 'Other defect/syndrome not already reported, specify'),
)

RANDOMIZATION_MATERNAL_ART_STATUS = (
    ('ON', 'On Haart'),
    ('OFF', 'Off'),
)


RANDOMIZATION_MATERNAL_FEEDING_CHOICE = (
    ('FF', 'Formula'),
    ('BF', 'Breast'),
)

RANDOMIZATION_SITE = (
    ('Molepolole', 'Molepolole'),
    ('Lobatse', 'Lobatse'),
    ('Gaborone', 'Gaborone'),
)

REASON_RCV_FORMULA = (
    ('no milk', '1. Mother did not have enough breast milk'),
    ('back to work', '2. Mother returned to work so unable to breastfeed participant exclusively'),
    ('off HAART', '3. Mother stopped breastfeeding because no longer taking HAART'),
    ('afraid to transmit', ('4. Mother stopped because she is afraid she will transmit HIV '
                            'to the participant even though she\'s taking HAART')),
    ('advised to mix feed', '5. Mother advised to add other food/liquids by partner/family'),
    ('felt to mix feed', ('6. Mother felt that baby needed other foods/liquids to be healthy '
                          '(for babies <= 6 months old)')),
    ('complete per protocol', ('7. <Per breastfeeding randomisation, infant is >5 months or >11 '
                               'months of age and completed breastfeeding per protocol')),
    (OTHER, '9. Other'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

REASON_MISSED_CTX_PLACEBO = (
    ('caregiver forgot', 'Caregiver forgot to give the CTX/Placebo'),
    ('caregiver ran out/lost', 'Caregiver ran out of CTX/Placebo or lost the bottle'),
    ('caregiver away',
     'Primary caregiver was away from home and did not have another person give the CTX/Placebo'),
    ('infant away', 'Infant was away from home and the CTX/Placebo bottle was not at the other location'),
    ('caregiver decision/sick',
     'Caregiver chose not to give the CTX/Placebo because baby was sick or for other reasons'),
    (OTHER, 'Other'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

REASONS_VACCINES_MISSED = (
    ('missed scheduled vaccination', 'Mother or Caregiver has not yet taken infant '
        'to clinic for this scheduled vaccination'),
    ('caregiver declines vaccination', 'Mother or Caregiver declines this vaccicnation'),
    ('no stock', 'Stock out at clinic'),
    (OTHER, 'Other, specify'),
)

REASON_MISSED_PROPHYLAXIS = (
    ('caregiver forgot', 'Caregiver forgot to give the NVP'),
    ('caregiver ran out/lost', 'Caregiver ran out of NVP or lost the bottle'),
    ('caregiver away', 'Primary caregiver was away from home and did not have another person give the NVP'),
    ('infant away', 'Infant was away from home and the NVP bottle was not at the other location'),
    ('caregiver decision/sick', 'Caregiver chose not to give the NVP because baby was sick or for other reasons'),
    (OTHER, 'Other'),
)

RENAL_ANOMALY = (
    ('None', 'None'),
    ('Bilateral renal agenesis', 'Bilateral renal agenesis'),
    ('Unilateral renal agenesis or dysplasia', 'Unilateral renal agenesis or dysplasia'),
    ('Polycystic kidneys', 'Polycystic kidneys'),
    ('Congenital hydronephrosis', 'Congenital hydronephrosis'),
    ('Unilateral stricture, stenosis, or hypoplasia', 'Unilateral stricture, stenosis, or hypoplasia'),
    ('Duplicated kidney or collecting system', 'Duplicated kidney or collecting system'),
    ('Horseshoe kidney', 'Horseshoe kidney'),
    ('Exstrophy of bladder', 'Exstrophy of bladder'),
    ('Posterior urethral valves', 'Posterior urethral valves'),
    (OTHER, 'Other renal, ureteral, bladder, urethral abnormality, specify'),
)

RESPIRATORY_DEFECT = (
    ('None', 'None'),
    ('Choanal atresia', 'Choanal atresia'),
    ('Agenesis or underdevelopment of nose', 'Agenesis or underdevelopment of nose'),
    ('Nasal cleft', 'Nasal cleft'),
    ('Single nostril, proboscis', 'Single nostril, proboscis'),
    ('OTHER nasal or sinus abnormality', 'Other nasal or sinus abnormality, specify'),
    ('Lryngeal web. glottic or subglottic', 'Lryngeal web. glottic or subglottic'),
    ('Congenital laryngeal stenosis', 'Congenital laryngeal stenosis'),
    ('OTHER laryngeal, tracheal or bronchial anomalies', 'Other laryngeal, tracheal or bronchial anomalies'),
    ('Single lung cyst', 'Single lung cyst'),
    ('Polycystic lung', 'Polycystic lung'),
    (OTHER, 'Other respiratory anomaly, specify'),
)

STUDY_STATUS = (
    ('followup', 'Lost can followup'),
    ('no followup', 'Lost no followup'),
)

SKIN_ABNORMALITY = (
    ('None', 'None'),
    ('Icthyosis', 'Icthyosis'),
    ('Ectodermal dysplasia', 'Ectodermal dysplasia'),
    (OTHER, 'Other skin abnormality, specify'),
)

TIMES_BREASTFED = (
    ('<1 per week', '1. Less than once per week'),
    ('<1 per day, but at least once per week', '2. Less than once per day, but at least once per week'),
    ('about 1 per day on most days', '3. About once per day on most days'),
    ('>1 per day, but not for all feedings', '4. More than once per day, but not for all feedings'),
    ('For all feedings', '5. For all feedings (i.e no formula or other foods or liquids)'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

TRISOME_CHROSOMESOME_ABNORMALITY = (
    ('None', 'None'),
    ('Trisomy 21', 'Trisomy 21'),
    ('Trisomy 13', 'Trisomy 13'),
    ('Trisomy 18', 'Trisomy 18'),
    ('OTHER trisomy, specify', 'Other trisomy, specify'),
    ('OTHER non-trisomic chromosome', 'Other non-trisomic chromosome abnormality, specify'),
)

VACCINES = (
    ('HBV', 'HBV'),
    ('BCG', 'BCG'),
    ('DTap', 'DTap'),
    ('Hib', 'Hib'),
    ('Polio', 'Polio'),
    ('Pneumoccal_Vaccine', 'Pneumoccal Vaccine'),
    ('Rotavirus', 'Rotavirus'),
    ('MMR', 'MMR'),
    ('Varicella', 'Varicella'),
    ('Influenza', 'Influenza'),
)

WATER_USED = (
    ('Water direct from source', 'Water direct from source'),
    ('Water boiled immediately before use', 'Water boiled immediately before use'),
    ('Water boiled earlier and then stored', 'Water boiled earlier and then stored'),
    ('Specifically treated water', 'Specifically treated water'),
    (OTHER, 'Other (specify)'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

ALIVE_DEAD_UNKNOWN = (
    ('ALIVE', 'Alive'),
    ('DEAD', 'Deceased'),
    ('UNKNOWN', 'Unknown'),
)

STOOL_TEXTURE_DESC = (
    ('formed_with_blood', 'Formed without blood'),
    ('formed_without_blood', 'Formed with blood'),
    ('loose_without_blood', 'Loose but not watery and without blood'),
    ('loose_with_blood', 'Loose but not watery and with blood'),
    ('watery_without_blood', 'Watery without blood'),
    ('watery_with_blood', 'Watery with blood'),
)

ILLNESS_CLASSIFICATION = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('respi_illness', 'Respiratory Illness'),
    ('gastro_illness', 'Gastrointestinal illness (examples including vomiting, diarrhea or both)'),
    (OTHER, 'Other'),
)

STOOLS_PAST_24HOURS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('>7', '>7'),
    (UNKNOWN, 'Unknown')
)

CONTINUOUS_LOOSE_STOOLS = (
    ('1day', '1 day'),
    ('2days', '2 days'),
    ('3days', '3 days'),
    ('4days', '4 days'),
    ('5days', '5 days'),
    ('6days', '6 days'),
    ('7days', '7 days'),
    ('>7days', 'Greater than 7 days but not more than 13 days'),
    ('>14days', '14 days or greater')
)

ARV_STATUS_WITH_NEVER = (
    (NO_MODIFICATIONS, '1. No modifications made since the last attended scheduled visit or today'),
    (START, '2. Starting today or has started since last attended scheduled visit'),
    ('discontinued', '3. Permanently discontinued at or before the last attended scheduled visit'),
    ('never started', '4. Never started'),
    ('modified', '5. Change in at least one medication since the last attended scheduled visit or today'),
    (NOT_APPLICABLE, 'Not applicable'),
)

CIRCUMCISION = (
    ('CIRC', 'circumcised'),
    ('UNCIRC', 'uncircumcised'),
)

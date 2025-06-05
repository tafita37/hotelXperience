# 📘 hotelXperience

## 1. Overview

### 📝 Project description
HotelXperience is a modular hotel management platform composed of a core hotel module and a dependent booking module that handles room reservations and customer interactions via a web portal. It allows clients to book and customize their stay while staff manage availability and pricing through a back-office interface.

### 🎯 Objective
HotelXperience provide a seamless, user-friendly platform for hotel room management and reservation, enabling clients to easily book rooms and customize their stay, while offering hotel staff efficient tools to manage room availability, pricing, and customer interactions.

---

## 2. Features

### ✅ Features list

<!-- - Manager side:
    - CRUD for Disease Type
    - CRUD for Disease
    - CRUD for Symptom
    - CRUD for Medication
    - List of patients held on site
    - List of requests + assignment to a nurse
    - List of nurses with the number of requests each needs to handle
- Patient side:
    - Request form
    - View their status
- Doctor side:
    - Prescription form + final action
    - List of medication recommendations during treatment
    - View records with the same symptom as a disease
    - Final action
    - List of consultations
    - Export patient record to PDF
- Nurse side:
    - List of requests + assignment to a doctor to create a consultation
    - Daily and weekly rounds (filter: done/to be done)
    - Create a round
    - Click on a round to release a patient or reschedule it and change the status
    - Export weekly round report to PDF -->


---

## 3. Requirements

### 🛠️ Required environment
- **Operating System**: Windows / macOS / Linux
- **Languages & Frameworks**: Odoo 18, Python 3.11.9
- **Database**: PostgreSQL

---

## 4. Installation

🔧 Installation instructions :

### Clone the repository
```bash
git clone https://github.com/tafita37/hotelXperience.git
```

### Setup the project in the Odoo modules directory, create a virtual environment, install dependencies, and run the project:

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python odoo-bin -c odoo.conf -u <module_name> -d <base_name> --dev xml
```
# DASHBOARD_WITH_FUNCTIONALITIES-OF-PALLE-TECHNOLOGYES


---

**Welcome to Palle Dashboard**

---

### 1. Introduction

The **Palle Admin Project** is a **role-based access control (RBAC)** system built with Django for managing employees and students. It supports two user types:

* **Admin** – Full permissions
* **Sales** – Limited access

---

### 2. System Components & Workflow

#### 2.1 User Roles & Permissions

**Admin (Superuser/Full Control):**

* Can view, add, update, and delete employees and students
* Full access to Admin Dashboard
* Can assign a student to any employee via the `added_by` dropdown

**Sales (Restricted Access):**

* Can add new students and view student list (read-only)
* Cannot modify/delete students or view employees
* `added_by` is auto-filled with their own username

#### 2.2 Authentication & Login Flow

* **Superuser Creation:** Done using Django’s `createsuperuser` command
* **Role-Based Redirect:**

  * Admins → Admin Dashboard
  * Sales → Sales Dashboard
* **Welcome Message:** Displays `"Welcome, [Username]"`

---

### 3. Functionality

#### 3.1 Admin Dashboard Features

**Navbar Options:**

* Employee List (View/Add/Delete)
* Student List (View/Edit/Delete)
* Logout

**Student Creation:**

* `added_by` field is a dropdown with all employees

#### 3.2 Sales Dashboard Features

**Navbar Options:**

* Add Student (Form submission)
* View Student List (Read-only)
* Logout

**Student Creation:**

* `added_by` field is auto-filled with the logged-in username

---

### 4. Technical Highlights

* **Django ORM:** Used for all database operations (`.filter()`, `.get()`, `.create()`, `.update()`)
* **Function-Based Views (FBVs):** All logic implemented using FBVs for control and customization
* **ModelForms:** Used for form creation and input validation
* **Role Handling Logic:** Handled in FBVs using `request.user` role-based checks
* **Django Admin Panel:** Extended for backend management (list display, filters, inline edits)
* **Session & Message Framework:** Used for login tracking and success/error messaging

---

### 5. Security & Data Integrity

* **Role-Based Access:** Sales users restricted from admin-only features
* **Field Control:** `added_by` field protected from manipulation
* **CSRF Protection:** Enabled on all POST forms
* **Session Handling:** Secure login/logout, proper redirects, and session protections

---

### 6. Technology Stack

* **Backend:** Python, Django (FBVs, ORM, authentication)
* **Frontend:** Django Templates, HTML, Bootstrap, CSS
* **Database:** MySQL with normalized schema and constraints

---

### 7. Summary

* Admin users have full CRUD access
* Sales users have limited access (add + read-only)
* Dashboards are role-specific
* Secure, clean handling of student assignments via `added_by`
* Django ORM and Function-Based Views used for all logic
* Forms built with ModelForms for validation
* Admin site utilized for backend data management

---

Pycache is evil, like bad cockroaches
(see
https://stackoverflow.com/questions/50752302/python3-pycache-generating-even-if-pythondontwritebytecode-1
)


as_view no longer necessary
It hates the about template being referenced in base
the CSS is 404, think it is a static pointing issue

don't think about is valid, getting an about not found, not valid view function/pattern name for no reverse match reasons

we have 14 tables:
                   List of relations
 Schema |            Name            | Type  |   Owner   
--------+----------------------------+-------+-----------
 public | auth_group                 | table | kassandra
 public | auth_group_permissions     | table | kassandra
 public | auth_permission            | table | kassandra
 public | auth_user                  | table | kassandra
 public | auth_user_groups           | table | kassandra
 public | auth_user_user_permissions | table | kassandra
 public | django_admin_log           | table | kassandra
 public | django_content_type        | table | kassandra
 public | django_migrations          | table | kassandra
 public | django_session             | table | kassandra
 public | main_app_patient           | table | kassandra
 public | main_app_patientrequest    | table | kassandra
 public | main_app_provider          | table | kassandra
 public | main_app_scheduler         | table | kassandra



 1) auth_group - 2 columns, id and name
id | name 
----+------
(0 rows)

 2) auth_group_permisions - 3 columns
id | group_id | permission_id 
----+----------+---------------
(0 rows)

3)auth_permission - 4 columns, 40 rows
 id |            name            | content_type_id |       codename        
----+----------------------------+-----------------+-----------------------
  1 | Can add log entry          |               1 | add_logentry
  2 | Can change log entry       |               1 | change_logentry
  3 | Can delete log entry       |               1 | delete_logentry
  4 | Can view log entry         |               1 | view_logentry
  5 | Can add permission         |               2 | add_permission
  6 | Can change permission      |               2 | change_permission
  7 | Can delete permission      |               2 | delete_permission
  8 | Can view permission        |               2 | view_permission
  9 | Can add group              |               3 | add_group
 10 | Can change group           |               3 | change_group
 11 | Can delete group           |               3 | delete_group
 12 | Can view group             |               3 | view_group
 13 | Can add user               |               4 | add_user
 14 | Can change user            |               4 | change_user
 15 | Can delete user            |               4 | delete_user
 16 | Can view user              |               4 | view_user
 17 | Can add content type       |               5 | add_contenttype
 18 | Can change content type    |               5 | change_contenttype
 19 | Can delete content type    |               5 | delete_contenttype
 20 | Can view content type      |               5 | view_contenttype
 21 | Can add session            |               6 | add_session
 22 | Can change session         |               6 | change_session
 23 | Can delete session         |               6 | delete_session
 24 | Can view session           |               6 | view_session
 25 | Can add patient            |               7 | add_patient
 26 | Can change patient         |               7 | change_patient
 27 | Can delete patient         |               7 | delete_patient
 28 | Can view patient           |               7 | view_patient
 29 | Can add patient request    |               8 | add_patientrequest
 30 | Can change patient request |               8 | change_patientrequest
 31 | Can delete patient request |               8 | delete_patientrequest
 32 | Can view patient request   |               8 | view_patientrequest
 33 | Can add provider           |               9 | add_provider
 34 | Can change provider        |               9 | change_provider
 35 | Can delete provider        |               9 | delete_provider
 36 | Can view provider          |               9 | view_provider
 37 | Can add scheduler          |              10 | add_scheduler
 38 | Can change scheduler       |              10 | change_scheduler
 39 | Can delete scheduler       |              10 | delete_scheduler
 40 | Can view scheduler         |              10 | view_scheduler
(40 rows)

4) auth_user - 11 columns
id | password | last_login | is_superuser | username | first_name last_name | email | is_staff | is_active | date_joined 

5) auth_user_groups - 3 columns
 id | user_id | group_id 
----+---------+----------
(0 rows)

6)auth_user_user_permissions - 3 columns
id | user_id | permission_id 
----+---------+---------------
(0 rows)

7-10)
django_admin_log   
django_content_type
django_migrations  
django_session     

are somewhat less significant in my eye.
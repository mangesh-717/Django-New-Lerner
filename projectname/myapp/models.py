from django.db import models

# Create your models here.


class Candidate(models.Model):
    full_name = models.CharField(max_length=55)
    Job_type = [
        ('Backend_Developer', 'Backend Developer'),
        ('Frontend Developer', 'Frontend Developer'),
        ('Full_Stack_Developer', 'Full Stack Developer'),
        ('Data_Scientist', 'Data_Scientist'),
        ('DevOps_Engineer', 'DevOps Engineer'),
        ('QA_Engineer', 'QA_Engineer'),
        ('Project_Manager', 'Project Manager'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Fluter_Developer', 'Fluter_developer'),
        ('MERN Developer', 'MERN_developer'),
        ('Digital Marketing', 'Digital Marketing'),]
    job_title = models.CharField(max_length=255, choices=Job_type)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,blank=True , null=True)
    github_id = models.URLField(blank=True, null=True)
    linkedin_id = models.URLField(blank=True, null=True)
    employment_detail = models.TextField(blank=True, null=True)
    technical_skills = models.TextField(blank=True, null=True)
    soft_skills = models.TextField(blank=True, null=True)
    year_of_experience = models.CharField(max_length=55 , null=True , blank=True)
    resume = models.FileField(upload_to='Resumes/', blank=True, null=True)
    Resume_score=models.IntegerField(blank=True,null=True) 
    def __str__(self):
        return self.full_name if self.full_name else "Unnamed Candidate"

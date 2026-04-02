from django.contrib import admin
from .models import *



from django.contrib import admin
from .models import Candidate
from pymongo import MongoClient
import os


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'email', 'year_of_experience', 'Resume_score')

    def save_model(self, request, obj, form, change):
        # Create a dictionary of the object data
        data = {
            'full_name': obj.full_name,
            'job_title': obj.job_title,
            'email': obj.email,
            'phone_number': obj.phone_number,
            'github_id': obj.github_id,
            'linkedin_id': obj.linkedin_id,
            'employment_detail': obj.employment_detail,
            'technical_skills': obj.technical_skills,
            'soft_skills': obj.soft_skills,
            'year_of_experience': obj.year_of_experience,
            'Resume_score': obj.Resume_score,
        }
          
        print(data)
        # Handle the resume file if uploaded
        # if obj.resume:
        #     resume_path = obj.resume.path
        #     data['resume_file'] = os.path.basename(resume_path)
        


        # # Insert or update the document in MongoDB
        # if change:  # Update existing record
        #     collection.update_one(
        #         {'email': obj.email},  # Use email as a unique identifier
        #         {'$set': data},
        #         upsert=True  # If no record exists, create one
        #     )
        # else:  # Insert a new record
        #     collection.insert_one(data)

        # Skip the ORM save since we're handling storage in MongoDB
        # Optionally, prevent the admin from saving to the default DB
        # return  # This skips Django ORM's default save functionality

# Register the Candidate model with the custom admin class
admin.site.register(Candidate, CandidateAdmin)

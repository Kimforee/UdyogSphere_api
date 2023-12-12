from django.db import models
# models.py

class User(models.Model):
    CANDIDATE = 'candidate'
    RECRUITER = 'recruiter'

    ROLE_CHOICES = [
        (CANDIDATE, 'Candidate'),
        (RECRUITER, 'Recruiter'),
    ]

    UserID = models.AutoField(primary_key=True)
    # UserID = models.UUIDField(unique=True, default=uuid.uuid4,editable=False,)
    Username = models.CharField(max_length=255)
    
    Password = models.CharField(max_length=255)  # Hashed and salted password
    Email = models.EmailField()
    UserType = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=CANDIDATE,
    )
    def __str__(self):
        return f'{self.Username} - {self.get_UserType_display()}'

class Candidate(models.Model):
    CandidateID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'role': 'candidate'})
    FullName = models.CharField(max_length=255)
    Resume = models.FileField(upload_to='resumes/')
    # Other candidate-specific details

class Recruiter(models.Model):
    RecruiterID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    CompanyName = models.CharField(max_length=255)
    # Other recruiter-specific details

class Job(models.Model):
    JobID = models.AutoField(primary_key=True)
    RecruiterID = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    JobTitle = models.CharField(max_length=255)
    JobDescription = models.TextField()
    Location = models.CharField(max_length=255)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    # Other job-specific details

class Application(models.Model):
    ApplicationID = models.AutoField(primary_key=True)
    JobID = models.ForeignKey(Job, on_delete=models.CASCADE)
    CandidateID = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    ApplicationDate = models.DateField(auto_now_add=True)
    Status = models.CharField(max_length=20)  # "Pending", "Accepted", "Rejected"

class Message(models.Model):
    MessageID = models.AutoField(primary_key=True)
    SenderID = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    ReceiverID = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    MessageContent = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True)


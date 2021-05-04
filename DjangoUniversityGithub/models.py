from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    courseNumber = models.IntegerField(default=0)
    instructorName = models.CharField(max_length=60)
    duration = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)

    objects = models.Manager()



    def __str__(self):
        return self.title

#inserts objects into table

sociology = djangoClasses(
    title="Sociology",
    courseNumber="101",
    instructorName="Mr. James",
    duration="90"
)
psychology = djangoClasses(
    title="Psychology",
    courseNumber="101",
    instructorName="Mr. Freud",
    duration="90"
)
philosophy = djangoClasses(
    title="Philosophy",
    courseNumber="101",
    instructorName="Mr. Rogan",
    duration="20"
)

djangoClasses_list = [sociology, psychology, philosophy]
djangoClasses.objects.bulk_create(djangoClasses_list)




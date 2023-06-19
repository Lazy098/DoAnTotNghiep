from django.core.management.base import BaseCommand
from user.models import Course
import json

class Command(BaseCommand):
    help = 'Import courses from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path) as json_file:
            data = json.load(json_file)
            for item in data:
                course_fields = item['fields']
                contents = course_fields.pop('contents')
                course_instance = Course(**course_fields)
                course_instance.contents = json.dumps(contents)
                course_instance.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully imported course: {course_instance.title}'))
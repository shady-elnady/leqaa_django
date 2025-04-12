#!/bin/bash

#  Start Celery Worker
celery -A Config worker --loglevel=info


# Run the Celery Beat (for scheduled tasks)
celery -A Config beat -l info
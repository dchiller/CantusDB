from main_app.models import Chant
from django.core.management.base import BaseCommand

# This management command opens every chant in the database
# and saves it. In doing so, it triggers the on_chant_save()
# function for each chant, which populates several fields used
# to optimizing site performance including
# Chant.search_vectors, Chant.volpiano_notes, Chant.volpiano_intervals,
# Source.number_of_chants and Source.number_of_melodies.

# As of late November 2023, it is serving no immediate purpose.
# We're keeping it around, however, as a helpful tool in case additional
# functionality is added in `signals.py` and we need to update the value
# of some field for all chants in the database.

# Run with `python manage.py touch_all_chants`.


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        CHUNK_SIZE = 1_000
        chants = Chant.objects.all()
        chants_count = chants.count()
        start_index = 0
        while start_index <= chants_count:
            self.stdout.write(f"processing chunk with {start_index=}")
            chunk = chants[start_index : start_index + CHUNK_SIZE]

            for chant in chunk:
                chant.save()
            del chunk  # make sure we don't use too much RAM
            start_index += CHUNK_SIZE

        self.stdout.write(
            self.style.SUCCESS("Success! Command has run to completion.\n")
        )

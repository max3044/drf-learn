from django.db import models

# just convert number to latin numeral
def convert_to_latin(num):
   res = ""
   table = [
      (1000, "M"),
      (900, "CM"),
      (500, "D"),
      (400, "CD"),
      (100, "C"),
      (90, "XC"),
      (50, "L"),
      (40, "XL"),
      (10, "X"),
      (9, "IX"),
      (5, "V"),
      (4, "IV"),
      (1, "I"),
   ]
   for cap, roman in table:
      d, m = divmod(num, cap)
      res += roman * d
      num = m

   return res


SEASON_STATUSES = [

    ("END", 'Ended'),
    ("ACT", 'Active'),
    ("FUT", 'Future'),
]





# Create your models here.
class Season(models.Model):
    
    class Meta:

        verbose_name = "Season"
        verbose_name_plural = "Seasons"
        ordering = ["number"]

    title = models.CharField(max_length=255, blank=True, null=True, unique=True)
    
    slogan = models.CharField(max_length=255, blank=True, null=True, unique=True)
    
    number = models.PositiveSmallIntegerField(unique=True, blank=True, null=True)
  
    description = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=3, choices=SEASON_STATUSES, default="FUT")

    
    @property
    def season_minted_nfts_count(self):
        return Nft.objects.filter(season=self).count()


    @property
    def numeral(self):
        return convert_to_latin(self.number)


    # ON SAVE
    def save(self, *args, **kwargs):
        if not self.pk:
            
            # This code only happens if the objects is
            # not in the database yet. Otherwise it would
            # have pk

            # If don't specify number
            if not self.number:
                self.number = Season.objects.count() + 1

            # self.numeral = convert_to_latin(self.number)

        # normal behaviour
        super(Season, self).save(*args, **kwargs)


    def __str__(self):
        return f"Season #{self.number}"


class Nft(models.Model):

    season = models.ForeignKey(Season, on_delete=models.CASCADE)
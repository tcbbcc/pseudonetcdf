from MetaNetCDF import file_master
from CAMx.wind.Transforms import wind_center_time_cell
from CAMx.height_pressure.Transforms import height_pressure_center_time_plus, \
                                            height_pressure_center_time, \
                                            height_pressure_plus
from CAMx.temperature.Transforms import temperature_center_time
from CAMx.vertical_diffusivity.Transforms import vertical_diffusivity_center_time
from CAMx.humidity.Transforms import humidity_center_time
from CAMx.cloud_rain.Transforms import cloud_rain_center_time_plus, \
                                       cloud_rain_center_time, \
                                       cloud_rain_plus
def pypass_camx_met_master(wind_path,hp_path,temp_path,kv_path,hum_path,cr_path,rows,cols,endhour=True):
     windf=wind_center_time_cell(wind_path,rows,cols,outunit='km/h',endhour=endhour,forcestaggered=False)
     hpf=height_pressure_center_time_plus(hp_path,rows,cols,outunit={'HGHT':'km', 'PRES':'hPA'},endhour=endhour)
     tempf=temperature_center_time(temp_path,rows,cols,outunit={'AIRTEMP':'deg_F','SURFTEMP':'deg_F'},endhour=endhour)
     kvf=vertical_diffusivity_center_time(kv_path,rows,cols,outunit={'KV':'m**2/s'},endhour=endhour)
     humf=humidity_center_time(hum_path,rows,cols,outunit={'HUM':'ppm'},endhour=endhour)
     crf=cloud_rain_center_time_plus(cr_path,rows,cols,outunit={'CLOUD':'g/m**3','RAIN':'g/m**3','SNOW':'g/m**3','GRAUPEL':'g/m**3','PRECIP':'g/m**3','PRECIPRATE':'mm/h','COD':'None'},endhour=endhour)
     return file_master([windf,hpf,tempf,kvf,humf,crf])
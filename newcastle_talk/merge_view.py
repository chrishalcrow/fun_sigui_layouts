from spikeinterface_gui import run_mainwindow
import spikeinterface.full as si
import json

with open('paper_curation.json') as f:
    curation_dict = json.load(f)

analyzer = si.load_sorting_analyzer(
    '/home/nolanlab/Work/Harry_Project/derivatives/sub-M25_ses-D20_typ-OF1_srt-kilosort4_analyzer.zarr'
)

layout = {
    'zone1': ['probe', 'curation', 'unitlist', 'spikelist'],
    'zone2': ['merge'],
    'zone3': ['waveform'],
    'zone4': ['correlogram'],
    'zone5': ['spikeamplitude'],
    'zone6': ['spikerate'],
    'zone7': ['ndscatter'],
    'zone8': ['metrics'],
}

user_settings = {
    'waveform': {'overlap': False}
}

run_mainwindow(
    analyzer,
    layout=layout,
    curation=True,
    curation_dict = curation_dict,
)

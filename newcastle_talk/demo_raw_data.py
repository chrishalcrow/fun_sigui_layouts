from spikeinterface_gui import run_mainwindow
import spikeinterface.full as si

rec = si.read_openephys(
    '/Users/christopherhalcrow/Work/Harry_Project/fast_curate_demo/analyzers/M29_D28/Record Node 109')
pp_rec = si.aggregate_channels(si.bandpass_filter(
    si.common_reference(rec.split_by('group'))))

analyzer = si.load_sorting_analyzer(
    '/Users/christopherhalcrow/Work/Harry_Project/fast_curate_demo/analyzers/M29_D28/sub-29_ses-28_srt-kilosort4_full_analyzer.zarr')

layout = {
    'zone5': ['unitlist', 'spikelist'],
    'zone6': [],
    'zone3': ['waveform'],
    'zone4': ['probe'],
    'zone1': ['spikeamplitude', 'trace', 'tracemap'],
    'zone8': ['correlogram', 'maintemplate'],
}

run_mainwindow(
    analyzer,
    recording=pp_rec,
    layout=layout,
)

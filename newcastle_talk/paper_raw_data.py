from spikeinterface_gui import run_mainwindow
import spikeinterface.full as si

rec = si.read_openephys(
    '/Users/christopherhalcrow/Work/Harry_Project/fast_curate_demo/analyzers/M29_D28/Record Node 109')
pp_rec = si.aggregate_channels(si.bandpass_filter(
    si.common_reference(rec.split_by('group'))))

analyzer = si.load_sorting_analyzer(
    '/Users/christopherhalcrow/Work/Harry_Project/fast_curate_demo/analyzers/M29_D28/sub-29_ses-28_srt-kilosort4_full_analyzer.zarr')

layout = {
    'zone1': ['spikedepth'],
    'zone2': [],
    'zone3': ['waveform'],
    'zone4': ['trace'],
    'zone5': ['unitlist', 'probe'],
    'zone6': ['spikelist'],
    'zone8': ['tracemap'],
}

user_settings = {
    'waveform': {'overlap': True, 'plot_selected_spike': True}
}

run_mainwindow(
    analyzer,
    recording=pp_rec,
    layout=layout,
    user_settings=user_settings,
)

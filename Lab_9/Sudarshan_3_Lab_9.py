#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: year2
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import threading



class Sudarshan_3_Lab_9(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Sudarshan_3_Lab_9")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.varible_qtgui_chooser_0 = varible_qtgui_chooser_0 = 0
        self.variable_qtgui_range_0_0 = variable_qtgui_range_0_0 = 1000
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0 = 0
        self.samp_rate = samp_rate = 32000
        self.phase = phase = 5
        self.fc = fc = 15000
        self.Beta = Beta = 50

        ##################################################
        # Blocks
        ##################################################

        self._fc_range = qtgui.Range(1000, 1000000, 1, 15000, 200)
        self._fc_win = qtgui.RangeWidget(self._fc_range, self.set_fc, "fc", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fc_win)
        # Create the options list
        self._varible_qtgui_chooser_0_options = [0, 1]
        # Create the labels list
        self._varible_qtgui_chooser_0_labels = ['FM', 'FM']
        # Create the combo box
        self._varible_qtgui_chooser_0_tool_bar = Qt.QToolBar(self)
        self._varible_qtgui_chooser_0_tool_bar.addWidget(Qt.QLabel("Modulator_selector" + ": "))
        self._varible_qtgui_chooser_0_combo_box = Qt.QComboBox()
        self._varible_qtgui_chooser_0_tool_bar.addWidget(self._varible_qtgui_chooser_0_combo_box)
        for _label in self._varible_qtgui_chooser_0_labels: self._varible_qtgui_chooser_0_combo_box.addItem(_label)
        self._varible_qtgui_chooser_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._varible_qtgui_chooser_0_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._varible_qtgui_chooser_0_options.index(i)))
        self._varible_qtgui_chooser_0_callback(self.varible_qtgui_chooser_0)
        self._varible_qtgui_chooser_0_combo_box.currentIndexChanged.connect(
            lambda i: self.set_varible_qtgui_chooser_0(self._varible_qtgui_chooser_0_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._varible_qtgui_chooser_0_tool_bar)
        self._variable_qtgui_range_0_0_range = qtgui.Range(0, 20000, 200, 1000, 200)
        self._variable_qtgui_range_0_0_win = qtgui.RangeWidget(self._variable_qtgui_range_0_0_range, self.set_variable_qtgui_range_0_0, "fm", "eng", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_qtgui_range_0_0_win)
        # Create the options list
        self._variable_qtgui_chooser_0_options = [0, 1]
        # Create the labels list
        self._variable_qtgui_chooser_0_labels = ['0', 'square']
        # Create the combo box
        self._variable_qtgui_chooser_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_0_tool_bar.addWidget(Qt.QLabel("waveform" + ": "))
        self._variable_qtgui_chooser_0_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_0_tool_bar.addWidget(self._variable_qtgui_chooser_0_combo_box)
        for _label in self._variable_qtgui_chooser_0_labels: self._variable_qtgui_chooser_0_combo_box.addItem(_label)
        self._variable_qtgui_chooser_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_options.index(i)))
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self._variable_qtgui_chooser_0_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_0(self._variable_qtgui_chooser_0_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._variable_qtgui_chooser_0_tool_bar)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            480000, #samp_rate
            "Frequency Modulated", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(False)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
            16384, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            480000, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self._phase_range = qtgui.Range(1, 100, 4, 5, 200)
        self._phase_win = qtgui.RangeWidget(self._phase_range, self.set_phase, "phase_sensitivity", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._phase_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, 480000,True)
        self.blocks_selector_0_0 = blocks.selector(gr.sizeof_gr_complex*1,0,0)
        self.blocks_selector_0_0.set_enabled(True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_float*1,0,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(480000, analog.GR_SQR_WAVE, 1000, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(480000, analog.GR_SIN_WAVE, 1000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 15000, 1, 0, 0)
        self.analog_phase_modulator_fc_0 = analog.phase_modulator_fc(5)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(5)
        self._Beta_range = qtgui.Range(0, 100, 5, 50, 200)
        self._Beta_win = qtgui.RangeWidget(self._Beta_range, self.set_Beta, "Frequency_Mudulation_index", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Beta_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.blocks_selector_0_0, 1))
        self.connect((self.analog_phase_modulator_fc_0, 0), (self.blocks_selector_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_selector_0, 1))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.analog_phase_modulator_fc_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_selector_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Sudarshan_3_Lab_9")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_varible_qtgui_chooser_0(self):
        return self.varible_qtgui_chooser_0

    def set_varible_qtgui_chooser_0(self, varible_qtgui_chooser_0):
        self.varible_qtgui_chooser_0 = varible_qtgui_chooser_0
        self._varible_qtgui_chooser_0_callback(self.varible_qtgui_chooser_0)

    def get_variable_qtgui_range_0_0(self):
        return self.variable_qtgui_range_0_0

    def set_variable_qtgui_range_0_0(self, variable_qtgui_range_0_0):
        self.variable_qtgui_range_0_0 = variable_qtgui_range_0_0

    def get_variable_qtgui_chooser_0(self):
        return self.variable_qtgui_chooser_0

    def set_variable_qtgui_chooser_0(self, variable_qtgui_chooser_0):
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc

    def get_Beta(self):
        return self.Beta

    def set_Beta(self, Beta):
        self.Beta = Beta




def main(top_block_cls=Sudarshan_3_Lab_9, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()

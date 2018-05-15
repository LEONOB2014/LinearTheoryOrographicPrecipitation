# -*- coding: utf-8 -*-

"""
/***************************************************************************
 LTOrographicPrecipitation
                                 A QGIS plugin
 Implements the Smith & Barstad (2004) LT model
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2018-05-02
        copyright            : (C) 2018 by Andy Aschwanden and Constantine Khrulev
        email                : uaf-pism@alaska.edu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Andy Aschwanden and Constantine Khrulev'
__date__ = '2018-05-02'
__copyright__ = '(C) 2018 by Andy Aschwanden and Constantine Khrulev'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.core import QgsProcessingProvider
from .ltop_precipitation import LTOrographicPrecipitationAlgorithm
from .ltop_test_dem import LTOrographicPrecipitationTestInput

class LTOrographicPrecipitationProvider(QgsProcessingProvider):

    def __init__(self):
        QgsProcessingProvider.__init__(self)

        # Load algorithms
        self.alglist = [LTOrographicPrecipitationAlgorithm(), LTOrographicPrecipitationTestInput()]

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        pass

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """
        for alg in self.alglist:
            self.addAlgorithm( alg )

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'ltop'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short (e.g. "Lastools") and localised.
        """
        return self.tr('Linear Theory Orographic Precipitation')

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return self.name()
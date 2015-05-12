<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>JRC_CLIMATE_ZONE</sld:Name>
            <sld:Title/>
            <sld:FeatureTypeStyle>
                <sld:Name/>
                <sld:Rule>
                    <sld:RasterSymbolizer>
                        <sld:Geometry>
                            <ogc:PropertyName>grid</ogc:PropertyName>
                        </sld:Geometry>
                        <sld:Opacity>1</sld:Opacity>
                        <sld:ColorMap>
                            <sld:ColorMapEntry color="#ffffff" label="No Data" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#df0015" label="1 - Warm temperate moist" opacity="1.0" quantity="1"/>
                            <sld:ColorMapEntry color="#d4002a" label="2 - Warm temperate dry" opacity="1.0" quantity="2"/>
                            <sld:ColorMapEntry color="#bf003f" label="3 - Cool temperate moist" opacity="1.0" quantity="3"/>
                            <sld:ColorMapEntry color="#aa0055" label="4 - Cool temperate dry" opacity="1.0" quantity="4"/>
                            <sld:ColorMapEntry color="#94006a" label="5 - Polar moist" opacity="1.0" quantity="5"/>
                            <sld:ColorMapEntry color="#7f007f" label="6 - Polar dry" opacity="1.0" quantity="6"/>
                            <sld:ColorMapEntry color="#6a0094" label="7 - Boreal moist" opacity="1.0" quantity="7"/>
                            <sld:ColorMapEntry color="#5500aa" label="8 - Boreal dry" opacity="1.0" quantity="8"/>
                            <sld:ColorMapEntry color="#3f00bf" label="9 - Tropical montane" opacity="1.0" quantity="9"/>
                            <sld:ColorMapEntry color="#2a00d4" label="10 - Tropical wet" opacity="1.0" quantity="10"/>
                            <sld:ColorMapEntry color="#1500e9" label="11 - Tropical moist" opacity="1.0" quantity="11"/>
                            <sld:ColorMapEntry color="#0c00ff" label="12 - Tropical dry" opacity="1.0" quantity="12"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>

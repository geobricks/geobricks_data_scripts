<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>Burning_AllForests_N2O_EF</sld:Name>
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
                            <sld:ColorMapEntry color="#fffefe" label="g/kg Dry Matter" opacity="0.00000001" quantity="0.00000001"/>
                            <sld:ColorMapEntry color="#ffffff" label="No Data" opacity="0.00000001" quantity="0.00000001"/>
                            <sld:ColorMapEntry color="#064308" label="Extra Tropical Forests: 0.2" opacity="1.0" quantity="0.2"/>
                            <sld:ColorMapEntry color="#a8ff36" label="Tropical Forests: 0.26" opacity="1.0" quantity="0.26"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>

<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>Cultivation_OrganicSoils_Area</sld:Name>
            <sld:Title/>
            <sld:FeatureTypeStyle>
                <sld:Name/>
                <sld:Rule>
                    <sld:RasterSymbolizer>
                        <sld:Geometry>
                            <ogc:PropertyName>grid</ogc:PropertyName>
                        </sld:Geometry>
                        <sld:Opacity>1</sld:Opacity>
                        <sld:ColorMap type="intervals">
                            <sld:ColorMapEntry color="#ffffff" label="ha (Hectares)" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#ffffff" label="No Data" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#006b00" label="0 - 10" opacity="1.0" quantity="10"/>
                            <sld:ColorMapEntry color="#c5db00" label="10 - 25" opacity="1.0" quantity="25"/>
                            <sld:ColorMapEntry color="#ffd900" label="25 - 40" opacity="1.0" quantity="40"/>
                            <sld:ColorMapEntry color="#ff8400" label="40 - 60" opacity="1.0" quantity="60"/>
                            <sld:ColorMapEntry color="#ff2600" label="60 - 90" opacity="1.0" quantity="90"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>

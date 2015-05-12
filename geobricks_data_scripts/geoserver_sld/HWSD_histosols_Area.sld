<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>HWSD_histosols_Area</sld:Name>
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
                            <sld:ColorMapEntry color="#edf8fb" label="Very Low (&gt;0 - 5,000)" opacity="1.0" quantity="5000"/>
                            <sld:ColorMapEntry color="#b3cde3" label="Low (5,000 - 15,000)" opacity="1.0" quantity="15000"/>
                            <sld:ColorMapEntry color="#8c96c6" label="Average (15,000 - 30,000)" opacity="1.0" quantity="30000"/>
                            <sld:ColorMapEntry color="#8856a7" label="High (30,000 - 45,000)" opacity="1.0" quantity="45000"/>
                            <sld:ColorMapEntry color="#810f7c" label="Very High (45,000 - 60,000)" opacity="1.0" quantity="61000"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>

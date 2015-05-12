<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>N2O_Emissions_Cultivation_OrganicSoils</sld:Name>
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
                            <sld:ColorMapEntry color="#ffffff" label="Gg" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#ffffff" label="No Data" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#00610c" label="0 - 0.10" opacity="1.0" quantity="0.1"/>
                            <sld:ColorMapEntry color="#8bb500" label="0.10 - 0.15" opacity="1.0" quantity="0.15"/>
                            <sld:ColorMapEntry color="#d7e600" label="0.15 - 0.20" opacity="1.0" quantity="0.2"/>
                            <sld:ColorMapEntry color="#ffe600" label="0.20 - 0.25" opacity="1.0" quantity="0.25"/>
                            <sld:ColorMapEntry color="#ffa600" label="0.25 - 0.30" opacity="1.0" quantity="0.3"/>
                            <sld:ColorMapEntry color="#ff6e00" label="0.30 - 0.35" opacity="1.0" quantity="0.35"/>
                            <sld:ColorMapEntry color="#ff2200" label="0.35 - 0.40" opacity="1.0" quantity="0.4"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>

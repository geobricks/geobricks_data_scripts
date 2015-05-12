<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>GEZ2010</sld:Name>
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
                            <sld:ColorMapEntry color="#78529c" label="Tropical rainforest" opacity="1.0" quantity="11"/>
                            <sld:ColorMapEntry color="#bd64a2" label="Tropical moist forest" opacity="1.0" quantity="12"/>
                            <sld:ColorMapEntry color="#c4a59f" label="Tropical dry frest" opacity="1.0" quantity="13"/>
                            <sld:ColorMapEntry color="#f5bcb8" label="Tropical shrubland" opacity="1.0" quantity="14"/>
                            <sld:ColorMapEntry color="#f29d1d" label="Tropical desert" opacity="1.0" quantity="15"/>
                            <sld:ColorMapEntry color="#fcb3fa" label="Tropical mountain system" opacity="1.0" quantity="16"/>
                            <sld:ColorMapEntry color="#5ab021" label="Subtropical humid forest" opacity="1.0" quantity="21"/>
                            <sld:ColorMapEntry color="#f2ea77" label="Subtropical dry forest" opacity="1.0" quantity="22"/>
                            <sld:ColorMapEntry color="#f7e5c3" label="Subtropical steppe" opacity="1.0" quantity="23"/>
                            <sld:ColorMapEntry color="#dbc49e" label="Subtropical desert" opacity="1.0" quantity="24"/>
                            <sld:ColorMapEntry color="#8ec976" label="Subtropical mountain system" opacity="1.0" quantity="25"/>
                            <sld:ColorMapEntry color="#b7e09f" label="Temperate oceanic forest" opacity="1.0" quantity="31"/>
                            <sld:ColorMapEntry color="#91b334" label="Temperate continental forest" opacity="1.0" quantity="32"/>
                            <sld:ColorMapEntry color="#fcc718" label="Temperate steppe" opacity="1.0" quantity="33"/>
                            <sld:ColorMapEntry color="#d7fcfc" label="Temperate desert" opacity="1.0" quantity="34"/>
                            <sld:ColorMapEntry color="#d8edda" label="Temperate mountain system" opacity="1.0" quantity="35"/>
                            <sld:ColorMapEntry color="#67b3b5" label="Boreal coniferous forest" opacity="1.0" quantity="41"/>
                            <sld:ColorMapEntry color="#4c8fc9" label="Boreal tundra woodland" opacity="1.0" quantity="42"/>
                            <sld:ColorMapEntry color="#b6d6d9" label="Boreal mountain system" opacity="1.0" quantity="43"/>
                            <sld:ColorMapEntry color="#b5b5b5" label="Polar" opacity="1.0" quantity="50"/>
                            <sld:ColorMapEntry color="#e7f6fa" label="Water" opacity="1.0" quantity="90"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>

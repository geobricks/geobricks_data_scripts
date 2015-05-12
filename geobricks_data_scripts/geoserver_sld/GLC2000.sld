<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>GLC2000</sld:Name>
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
                            <sld:ColorMapEntry color="#ffffff" label="GLC2000 Land Cover" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#ffffff" label="No Data" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#ffea9e" label="Herbaceous Cover, closed-open" opacity="1.0" quantity="13"/>
                            <sld:ColorMapEntry color="#decaa1" label="Sparse herbaceous or sparse shrub cover" opacity="1.0" quantity="14"/>
                            <sld:ColorMapEntry color="#009696" label="Regularly flooded shrub and/or herbaceous cover" opacity="1.0" quantity="15"/>
                            <sld:ColorMapEntry color="#ffe0e5" label="Cultivated and managed areas" opacity="1.0" quantity="16"/>
                            <sld:ColorMapEntry color="#ff75e8" label="Mosaic: Cropland / Tree Cover / Other natural vegetation" opacity="1.0" quantity="17"/>
                            <sld:ColorMapEntry color="#ca8aff" label="Mosaic: Cropland / Shrub and/or grass cover" opacity="1.0" quantity="18"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>
